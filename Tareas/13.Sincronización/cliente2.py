import socket
import sys
import thread
 
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9882))
r = socket.socket()
r.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

puerto = 9884
def mensaje(mm,puerto):
    mensajje = r.recv(1024)
    print 'mensajje'
t = False
j = False
numero1 = ''
while not t:
    
    if j == False:
        print('ingrese la operacion que desea: \n1. Para crear grupo \n2. Para unirse a un grupo' )
        numero1= raw_input("3. Para enviar un mensaje \n4. Para salir \n ")
        s.send(numero1+' '+str(puerto) + ' ' + '.')
        r.connect(('localhost',9884))
        j= True
    else:
        mensajje = r.recv(1024)
        print(mensajje)
        print('ingrese la operacion que desea: \n1. Para crear grupo \n2. Para unirse a un grupo' )
        numero1= raw_input("3. Para enviar un mensaje \n4. Para salir \n ")
    if int(numero1) == 4:
            t =True
    else:
            if int(numero1) == 1:
                    opcion = raw_input("Digite el nombre que desea para el grupo: ")
                    s.send(numero1+' '+str(puerto) + ' ' + opcion)
                    operacion=s.recv(1024)
            if int(numero1) == 2:
                    s.send(numero1+' '+str(puerto) + ' ' + '.')
                    operacion=s.recv(1024)
                    print operacion
                    opcion =  raw_input("Digite el numero del grupo que desea para el grupo: ")
                    s.send(numero1+' '+str(puerto)+' '+opcion)
                    operacion=s.recv(1024)
            elif int(numero1) == 3:
                    opcion =  raw_input("Digite el mensajeque desea enviar: ")
                    s.send(numero1+' '+str(puerto)+' '+opcion)
            print operacion



s.close()
r.close()
