import SocketServer
def potenciacion(numero1,numero2):
	return pow(numero1,numero2)

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		print self.mensajeRecibido
		self.valores=self.mensajeRecibido.split("@")
		self.potenciacion=str(potenciacion(int(self.valores[0]),int(self.valores[1])))
		print "los numeros recibidos son: ",self.valores[0],"y", self.valores[1], "y la potencia es:", self.potenciacion
		self.request.send(self.potenciacion)

def main():
	print "Servidor potenciacion"
	host="localhost"
	puerto=9993 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverPotenciacion corriendo"
	server1.serve_forever()

main()