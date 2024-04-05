# Atividade Ponderada - Projeto em Flask com interface de controle do robô
## Processo para inicializar a aplicação:
**0) Ativar ambiente virtual:**
É indicado a utilização de um ambiente virtual para rodar esta aplicação. Para isso deve-se criar dentro da pasta flask-htmx o venv, por meio do seguinte comando, no powershell:
`python -m venv venv`. Depois será necessário ativar esse ambiente, pelo seguinte comando: `cd venv\Scripts`, em seguida: `.\Activate`.</br>

**1) Instalando depedências:**
Para instalar as depedências devemos utilizar o seguinte comando: `pip install -r requirements.txt`.</br>

**2) Navegar até a pasta src**
Dentro da página flask-htmx vá até a pasta src: `cd src`, e depois execute o programa pelo seguinte comando: `python main.py`</br>

## Como utilizar a aplicação:
**- Se o robô estiver conectado**</br>
Você direcionado para uma página que lhe avisará que o robô não está conectado e que a única página que você pode visualizar é a `/logs`. Na rota `/logs` você conseguirá visualizar todas as vezes que houve uma requisição no botão mover na tela index. </br>

**- Se o robô não estiver conectado**</br>
Você será direcionado para a página index em que há um aviso de que o robô está conectado e após há um formulário em que é possível colocar os dados das coordenadas para que o robô se movimente, estas são: x, y, z, r. Há também um botão em que conseguimos resetar o banco de dados e um segundo forms que por meio do id selecionado ocnseguimos dar um update na mensagem escrita no banco de dados. </br>

## Link de demonstração do vídeo:</br>
https://youtu.be/5eo9MI2J6oA?si=KTCSWuytxACAcAQl


