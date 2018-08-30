import SocketServer
def resta(numero1,numero2):
	return numero1 - numero2

class miHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		print self.mensajeRecibido
		self.numero1,self.numero2,self.operador=self.mensajeRecibido.split("@")
		self.restan=str(resta(int(self.numero1),int(self.numero2)))
		print "los numeros recibidos son: ",self.numero1,"y", self.numero2, "y la resta es:", self.restan
		self.request.send(self.restan)

def main():
	print "Servidor Resta"
	host="localhost"
	puerto=9997 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "serverResta corriendo"
	server1.serve_forever()

main()