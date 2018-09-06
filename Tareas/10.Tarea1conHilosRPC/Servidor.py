from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time


class MyFuncts:
    def add(self,numero1,numero2):
        return int(numero1) + int(numero2)

    def sub(self, numero1,numero2):
        return int(numero1)-int(numero2)

    def mul(self, numero1,numero2):
        return int(numero1)*int(numero2)

    def div(self, numero1,numero2):
        return int(numero1)//int(numero2)

    def rad(self,numero1,numero2):
        numero2=1/int(numero2)
        return pow(int(numero1),numero2)

    def pow(self,numero1,numero2):
        return pow(int(numero1),int(numero2))

    def log(self,numero1,numero2):
        return math.log(int(numero1),int(numero2))
	
class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",9992))
         #self.localServer.register_function(div)
         self.localServer.register_instance(MyFuncts())

    def run(self):
         self.localServer.serve_forever()
"""
hilos=[] #adiciona todos los hilos
for i in range (7):
    hilos.append(ServerThread())

for hl in hilos: #pone a correr todos los hilos
    hl.start()
"""
server = ServerThread()
server.start() # The server is now running
print "Listo servidor."