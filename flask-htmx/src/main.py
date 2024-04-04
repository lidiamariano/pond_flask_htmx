from flask import Flask, render_template, request
from flask_cors import CORS
from tinydb import TinyDB, Query
from pydobot import Dobot
from serial.tools import list_ports

db = TinyDB("logs.json")

app = Flask(__name__)
CORS(app)

device = None

try:
    available_ports = list_ports.comports()
    if available_ports:
        port = available_ports[0].device
        device = Dobot(port=port, verbose=False)
        velocidade = device.speed(500, 500)
except Exception as e:
    print(f"Erro ao conectar ao dispositivo: {e}")

# Retorna o index.html
@app.route('/')
def index():
    if device is None:
        return 'O robô não está conectado! Você só pode acessar a rota /logs'
    return render_template('index.html')

if device is not None:
    @app.route('/print')
    def printar():
        db.insert({'log':'GET /print'})
        return '<h1>L</h1>'
    
    @app.route('/posicao')
    def posicao():
        db.insert({'log': 'GET posicao'})
        return f'<h1>{device.pose()}<h1>'
    
    @app.route('/mover', methods=['GET','POST'])
    def mover():
        if request.method == 'POST':
            x = request.form.get('x')
            y = request.form.get('y')
            z = request.form.get('z')
            r = request.form.get('r')
            
            db.insert({'log': 'POST posicoes'})
            device.move_to(float(x),float(y), float(z), float(r))
            return f'<h1>X: {x}, Y: {y}, Z: {z}</h1>'

    @app.route('/apagar-banco', methods=['POST'])
    def apagar_banco():
        if request.method == 'POST':
            db.truncate()
            return "Banco de dados apagado com sucesso."
    
    @app.route('/atualizar-banco', methods=['POST'])
    def atualizar_banco():
        if request.method == 'POST':
            log_id = request.form.get('log_id')
            new_log_text = request.form.get('new_log_text')
            if log_id is not None:
                db.update({'log': new_log_text}, doc_ids=[int(log_id)])
                return "Banco de dados atualizado com sucesso."
            else:
                return "Erro: log_id não foi fornecido."
        
@app.route('/logs')
def exibir_logs():
    logs = db.all()
    print(logs)
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
