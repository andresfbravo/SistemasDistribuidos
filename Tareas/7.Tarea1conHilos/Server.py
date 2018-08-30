import socket
import sys
import thread
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9999))
s.listen(10)

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

def connection(sc, addr):
	dato = sc.recv(1024)
	numero1,numero2,operacion=dato.split("@")
	print numero1,operacion,numero2

	if(operacion=="+"):
		suman=str(suma(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y suman: ",suman
		#request.send(suman)
		sc.send(str(int(suman)))
	elif(operacion=="-"):
		restan=str(resta(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y restan: ",restan
		sc.send(str(int(restan)))
	elif(operacion=="x" or operacion=="X"):
		multiplican=str(multiplicacion(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y multiplican: ",multiplican
		sc.send(str(int(multiplican)))
	elif(operacion=="/"):
		dividen=str(division(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y dividen: ",dividen
		sc.send(str(int(dividen)))
	elif(operacion=="raiz"):
		raiz=str(radicacion(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y su raiz es: ",raiz
		sc.send(str(int(raiz)))
	elif(operacion=="pow"):
		pow=str(potenciacion(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y su potencia es: ",pow
		sc.send(str(int(pow)))
	elif(operacion=="log"):
		log=str(logaritmacion(int(numero1),int(numero2)))
		print "los numeros recibidos son: ", numero1, "y", numero2," y su logaritmo es: ",log
		sc.send(str(int(log)))



while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))
    
sc.close()
s.close()