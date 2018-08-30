import SocketServer
def suma(numero1,numero2):
	return numero1 + numero2

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		self.valores=self.mensajeRecibido.split("@")
		self.suman=str(suma(int(self.valores[0]),int(self.valores[1])))
		print "los numeros recibidos son: ",self.valores[0],"y", self.valores[1], "y la suma es:", self.suman
		self.request.send(self.suman)

def main():
	print "Servidor Suma"
	host="localhost"
	puerto=9998 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverSuma corriendo"
	server1.serve_forever()

main()