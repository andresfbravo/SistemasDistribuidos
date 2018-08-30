import socket
import sys
import thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9995))
s.listen(10)

def divide(numero1,numero2):
	return numero1 // numero2

def connection(sc, addr):
	dato = sc.recv(1024)
	numero1,numero2,operacion=dato.split("@")
	print numero1,operacion,numero2
	dividen=divide(int(numero1),int(numero2))
	print "los numeros recibidos son: ", numero1, "y", numero2," y dividen: ",dividen
	sc.send(str(int(dividen)))


while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))
    
sc.close()
s.close()