import SocketServer
import math


def suma(numero1,numero2):
	return numero1+numero2

def resta(numero1,numero2):
	return numero1-numero2

def multiplicacion(numero1,numero2):
	return numero1*numero2

def division(numero1,numero2):
	return numero1/numero2

def radicacion(numero1,numero2):
	return pow(numero1,division(1,numero2))

def potenciacion(numero1,numero2):
	return pow(numero1,numero2)

def logaritmacion(numero1,numero2):
	return math.log(numero1,numero2)

class miHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.mensajeRecibido=str(self.request.recv(1024))
		#print self.mensajeRecibido
		self.numero1,self.numero2,self.operacion=self.mensajeRecibido.split("@")
		if(self.operacion=="+"):
			self.suman=str(suma(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y suman: ",self.suman
			self.request.send(self.suman)
		elif(self.operacion=="-"):
			self.restan=str(resta(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y restan: ",self.restan
			self.request.send(self.restan)
		elif(self.operacion=="x" or self.operacion=="X"):
			self.multiplican=str(multiplicacion(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y multiplican: ",self.multiplican
			self.request.send(self.multiplican)
		elif(self.operacion=="/"):
			self.dividen=str(division(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y dividen: ",self.dividen
			self.request.send(self.dividen)
		elif(self.operacion=="raiz"):
			self.raiz=str(radicacion(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y su raiz es: ",self.raiz
			self.request.send(self.raiz)
		elif(self.operacion=="pow"):
			self.pow=str(potenciacion(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y su potencia es: ",self.pow
			self.request.send(self.pow)
		elif(self.operacion=="log"):
			self.log=str(logaritmacion(int(self.numero1),int(self.numero2)))
			print "los numeros recibidos son: ", self.numero1, "y", self.numero2," y su logaritmo es: ",self.log
			self.request.send(self.log)

def main():
	print "Taller socket"
	host="localhost"
	puerto=9994 #entre 0 y 10000, por los 9000 no estan usados

	server1= SocketServer.TCPServer((host,puerto),miHandler)
	print "server corriendo"
	server1.serve_forever()

main()