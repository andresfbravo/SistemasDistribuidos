import socket
import sys
import thread

print "ServidorIntermedio"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(10)
host='localhost'

socketSuma = socket.socket()
socketSuma.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
puertoSuma=9998
socketSuma.connect((host, puertoSuma))#a suma

puertoResta=9997
socketResta.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketResta=socket.socket()
socketResta.connect((host,puertoResta))

puertoMultiplicacion=9996
socketMultiplicacion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketMultiplicacion=socket.socket()
socketMultiplicacion.connect((host,puertoMultiplicacion))

puertoDivision=9995
socketDivision.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketDivision=socket.socket()
socketDivision.connect((host,puertoDivision))

puertoRadicacion=9994
socketRadicacion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketRadicacion=socket.socket()
socketRadicacion.connect((host,puertoRadicacion))

puertoPotenciacion=9993
socketPotenciacion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketPotenciacion=socket.socket()
socketPotenciacion.connect((host,puertoPotenciacion))

puertoLogaritmacion=9992
socketLogaritmacion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketLogaritmacion=socket.socket()
socketLogaritmacion.connect((host,puertoLogaritmacion))

def connection(sc, addr):
	mensajeRecibido=str(sc.recv(1024))
	valores=mensajeRecibido.split("@")
	operador=valores[2]

	if(operador=="+"):
		socketSuma.send(mensajeRecibido)
		mensajeRespuesta=str(socketSuma.recv(1024))
		sc.send(mensajeRespuesta)
	elif(operador=="-"):
		socketResta.send(mensajeRecibido)
		mensajeRespuesta=str(socketResta.recv(1024))
		sc.send(mensajeRespuesta)
	elif(operador=="x"):
		socketMultiplicacion.send(mensajeRecibido)
		mensajeRespuesta=str(socketMultiplicacion.recv(1024))
		sc.send(mensajeRespuesta)
	elif(operador=="/"):
		socketDivision.send(mensajeRecibido)
		mensajeRespuesta=str(socketDivision.recv(1024))
		sc.send(mensajeRespuesta)
	elif(operador=="raiz"):
		socketRadicacion.send(mensajeRecibido)
		mensajeRespuesta=str(socketRadicacion.recv(1024))
		sc.send(mensajeRespuesta)
	elif(operador=="pow"):
		socketPotenciacion.send(mensajeRecibido)
		mensajeRespuesta=str(socketPotenciacion.recv(1024))
		sc.send(mensajeRespuesta)
	elif(operador=="log"):
		socketLogaritmacion.send(mensajeRecibido)
		mensajeRespuesta=str(socketLogaritmacion.recv(1024))
		sc.send(mensajeRespuesta)

while 1:

    sc, addr = s.accept()
    print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
    print "\n"
    thread.start_new_thread(connection,(sc,addr))
    
sc.close()
s.close()