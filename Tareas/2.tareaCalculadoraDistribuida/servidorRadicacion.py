import SocketServer
def radicacion(numero1,numero2):
	numero2=1/numero2
	return pow(numero1,numero2)

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		print self.mensajeRecibido
		self.valores=self.mensajeRecibido.split("@")
		self.radicacion=str(radicacion(int(self.valores[0]),int(self.valores[1])))
		print "los numeros recibidos son: ",self.valores[0],"y", self.valores[1], "y la raiz es:", self.radicacion
		self.request.send(self.radicacion)

def main():
	print "Servidor radicacion"
	host="localhost"
	puerto=9994 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverRadicacion corriendo"
	server1.serve_forever()

main()