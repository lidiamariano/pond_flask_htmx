import serial
import serial.tools.list_ports
from pydobot import Dobot

class RobotFinder:
    def __init__(self):
        pass

    def try_connect(self, port):
        try:
            with serial.Serial(port, timeout=1) as ser:
                # Verifica se o dispositivo responde a um comando de identificação
                ser.write(b"\x55\x55\x04\x01\x00\x59")  # Comando de identificação
                response = ser.read(6)  # Lê a resposta
                if len(response) == 6 and response[0] == 85 and response[1] == 85:
                    print(f"Conectado ao Dobot na porta {port}")
                    return Dobot(port=port)
                else:
                    print(f"Não foi possível conectar o Dobot à porta {port}")
                    return None
        except Exception as e:
            print(f"Erro ao conectar ao Dobot na porta {port}: {e}")
            return None

    def find_and_connect(self):
        found_dobot = None
        for port in serial.tools.list_ports.comports():
            dobot = self.try_connect(port.device)
            if dobot:
                found_dobot = dobot
                break
        if found_dobot is None:
            print("Nenhum Dobot encontrado.")
        return found_dobot