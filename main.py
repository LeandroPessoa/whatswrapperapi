from stack import YowsupSendStack
import time




from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/<string:numero>/<string:mensagem>')
def index(numero,mensagem):

	contato = numero + '@s.whatsapp.net'

	CREDENTIALS = ("553194769160", "ZHqncTGDLww/OVgHIBtdesG3oMs=") # replace with your phone and password
	#ultimo registro tem que ser null, é um marcador.
	mensagem = ((contato,mensagem),('null','null'))

	messenger = YowsupSendStack(CREDENTIALS, mensagem)

	resposta = messenger.start()

	time.sleep(10)

	return resposta
	

