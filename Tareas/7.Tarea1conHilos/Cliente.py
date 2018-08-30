import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9999))

print "\t\tSELECCIONE EL TIPO DE OPERACION QUE DESEA EFECTUAR E INGRESE LOS NUMEROS A OPERAR\n"
print "1.Suma\n"
print "2.Resta.\n"
print "3.Multiplicacion\n"
print "4.Division\n"
print "5.Radicacion\n"
print "6.Potenciacion\n"
print "7.Logaritmacion\n"
operacion=raw_input("\ningrese la operacion: ")
numero1=raw_input("\ningrese su numero: ")
numero2=raw_input("\ningrese otro numero: ")
#socket1.send(numero2)
if(operacion=="1"):
	operacion="+"
elif(operacion=="2"):
	operacion="-"
elif(operacion=="3"):
	operacion="x"
elif(operacion=="4"):
	operacion="/"
elif(operacion=="5"):
	operacion="raiz"
elif(operacion=="6"):
	operacion="pow"
elif(operacion=="7"):
	operacion="log"
mensaje=numero1+"@"+numero2+"@"+operacion
#print mensaje
s.send(mensaje)

resultado = s.recv(1024)
print "---------------------------------"
print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ", resultado
print "---------------------------------"

s.close()