import SocketServer
def division(numero1,numero2):
	return numero1 * numero2

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		print self.mensajeRecibido
		self.valores=self.mensajeRecibido.split("@")
		self.division=str(division(int(self.valores[0]),int(self.valores[1])))
		print "los numeros recibidos son: ",self.valores[0],"y", self.valores[1], "y la division es:", self.division
		self.request.send(self.division)

def main():
	print "Servidor Division"
	host="localhost"
	puerto=9995 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverDivision corriendo"
	server1.serve_forever()

main()