import socket
print "Taller 1"
host="localhost"
puerto=9994
socket1=socket.socket()
socket1.connect((host,puerto))

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
socket1.send(mensaje)
resultado=socket1.recv(1024)
print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ", resultado
tiempo=raw_input("presione enter para terminar")
socket1.close