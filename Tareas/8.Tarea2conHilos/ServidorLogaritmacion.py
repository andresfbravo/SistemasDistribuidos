import socket
import sys
import thread
import math
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9992))
s.listen(10)

def logatitma(numero1,numero2):
	return math.log(numero1,numero2)

def connection(sc, addr):
	dato = sc.recv(1024)
	numero1,numero2,operacion=dato.split("@")
	print numero1,operacion,numero2
	logatitman=logatitma(int(numero1),int(numero2))
	print "los numeros recibidos son: ", numero1, "y", numero2," y logatitman: ",logatitman
	sc.send(str(int(logatitman)))


while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))
    
sc.close()
s.close()