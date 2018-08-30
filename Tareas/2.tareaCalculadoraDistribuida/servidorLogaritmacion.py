import SocketServer
import math
def logaritmacion(numero1,numero2):
	return math.log(numero1,numero2)

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		print self.mensajeRecibido
		self.valores=self.mensajeRecibido.split("@")
		self.logaritmacion=str(logaritmacion(int(self.valores[0]),int(self.valores[1])))
		print "los numeros recibidos son: ",self.valores[0],"y", self.valores[1], "y su logaritmo es:", self.logaritmacion
		self.request.send(self.logaritmacion)

def main():
	print "Servidor logaritmacion"
	host="localhost"
	puerto=9992 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverPotenciacion corriendo"
	server1.serve_forever()

main()