import xmlrpclib
#instancio un objeto y conecto el servidor a donde se va a conectar
s = xmlrpclib.ServerProxy('http://localhost:9999')

def menu():
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
	if(operacion=="1"):
		operacion="+"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.add(numero1,numero2)
	elif(operacion=="2"):
		operacion="-"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.sub(numero1,numero2)
	elif(operacion=="3"):
		operacion="x"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.mul(numero1,numero2)
	elif(operacion=="4"):
		operacion="/"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.div(numero1,numero2)
	elif(operacion=="5"):
		operacion="rad"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.rad(numero1,numero2)
	elif(operacion=="6"):
		operacion="pow"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.pow(numero1,numero2)
	elif(operacion=="7"):
		operacion="log"
		print "La operacion de: ", numero1, " ",operacion," ", numero2," es: ",s.log(numero1,numero2)
	#print s.system.listMethods()

menu()