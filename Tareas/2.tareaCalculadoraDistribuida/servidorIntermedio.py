import socket
import SocketServer
#print "ServidorIntermedio"
host="localhost"#o localhost
puertoSuma=9998
socketSuma=socket.socket()
socketSuma.connect((host,puertoSuma))

puertoResta=9997
socketResta=socket.socket()
socketResta.connect((host,puertoResta))

puertoMultiplicacion=9996
socketMultiplicacion=socket.socket()
socketMultiplicacion.connect((host,puertoMultiplicacion))

puertoDivision=9995
socketDivision=socket.socket()
socketDivision.connect((host,puertoDivision))

puertoRadicacion=9994
socketRadicacion=socket.socket()
socketRadicacion.connect((host,puertoRadicacion))

puertoPotenciacion=9993
socketPotenciacion=socket.socket()
socketPotenciacion.connect((host,puertoPotenciacion))

puertoLogaritmacion=9992
socketLogaritmacion=socket.socket()
socketLogaritmacion.connect((host,puertoLogaritmacion))

#tiempo=raw_input("presione enter para terminar")
#socket1.close()

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		self.valores=self.mensajeRecibido.split("@")
		self.operador=self.valores[2]
		if(self.operador=="+"):
			socketSuma.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketSuma.recv(1024))
			self.request.send(self.mensajeRespuesta)
		elif(self.operador=="-"):
			socketResta.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketResta.recv(1024))
			self.request.send(self.mensajeRespuesta)
		elif(self.operador=="x"):
			socketMultiplicacion.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketMultiplicacion.recv(1024))
			self.request.send(self.mensajeRespuesta)
		elif(self.operador=="/"):
			socketDivision.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketDivision.recv(1024))
			self.request.send(self.mensajeRespuesta)
		elif(self.operador=="raiz"):
			socketRadicacion.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketRadicacion.recv(1024))
			self.request.send(self.mensajeRespuesta)
		elif(self.operador=="pow"):
			socketPotenciacion.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketPotenciacion.recv(1024))
			self.request.send(self.mensajeRespuesta)
		elif(self.operador=="log"):
			socketLogaritmacion.send(self.mensajeRecibido)
			self.mensajeRespuesta=str(socketLogaritmacion.recv(1024))
			self.request.send(self.mensajeRespuesta)
	
def main():
	print "Servidor Intermedio"
	host="localhost"
	puerto=9999 #entre 0 y 10000, por los 9000 no estan usados

	serverIntermedio= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverIntermedioCorriendo"
	serverIntermedio.serve_forever()

main()