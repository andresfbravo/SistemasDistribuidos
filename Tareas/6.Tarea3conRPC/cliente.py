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
	elif(operacion=="2"):
		operacion="-"
	elif(operacion=="3"):
		operacion="x"
	elif(operacion=="4"):
		operacion="/"
	elif(operacion=="5"):
		operacion="rad"
	elif(operacion=="6"):
		operacion="pow"
	elif(operacion=="7"):
		operacion="log"
	datos = numero1+"@"+numero2+"@"+operacion
	#print datos
	serverD = s.redireccionar(datos)
	if(serverD=='http://localhost:9998'):
		servidorSuma = xmlrpclib.ServerProxy('http://localhost:9998')
		print servidorSuma.add(numero1,numero2)
	elif(serverD=='http://localhost:9997'):
		servidorSub = xmlrpclib.ServerProxy('http://localhost:9997')
		print servidorSub.sub(numero1,numero2)
	elif(serverD=='http://localhost:9996'):
		servidorMul = xmlrpclib.ServerProxy('http://localhost:9996')
		print servidorMul.mul(numero1,numero2)
	elif(serverD=='http://localhost:9995'):
		servidorDiv = xmlrpclib.ServerProxy('http://localhost:9995')
		print servidorDiv.div(numero1,numero2)
	elif(serverD=='http://localhost:9994'):
		servidorRad = xmlrpclib.ServerProxy('http://localhost:9994')
		print servidorRad.rad(numero1,numero2)
	elif(serverD=='http://localhost:9993'):
		servidorPow = xmlrpclib.ServerProxy('http://localhost:9993')
		print servidorPow.pow(numero1,numero2)
	elif(serverD=='http://localhost:9992'):
		servidorLog = xmlrpclib.ServerProxy('http://localhost:9992')
		print servidorLog.log(numero1,numero2)

menu()