import SocketServer
def multiplicacion(numero1,numero2):
	return numero1 * numero2

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		print self.mensajeRecibido
		self.valores=self.mensajeRecibido.split("@")
		self.multiplicacion=str(multiplicacion(int(self.valores[0]),int(self.valores[1])))
		print "los numeros recibidos son: ",self.valores[0],"y", self.valores[1], "y la multiplicacion es:", self.multiplicacion
		self.request.send(self.multiplicacion)

def main():
	print "Servidor Multiplicacion"
	host="localhost"
	puerto=9996 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverMultiplicacion corriendo"
	server1.serve_forever()

main()