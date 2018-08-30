import SocketServer
def suma(numero1,numero2):
		return numero1 + numero2
class miHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.numero1=int(self.request.recv(1024)) 
		#de a 1024 datos se va a recibir
		self.numero2=int(self.request.recv(1024))
		self.suman=str(suma(self.numero1, self.numero2))
		print "los numeros recibidos son: ",self.numero1,"y", self.numero2, 
		      "y la suma entre ambos es: ",self.suman
		self.request.send(self.suman)

def main():
	print "Taller socket"
	host="localhost"
	puerto=9999   #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "server corriendo"
	server1.serve_forever()


main()
