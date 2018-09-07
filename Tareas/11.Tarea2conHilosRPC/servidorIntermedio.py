from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time

class MyFuncts:
    def pedir():
        pass

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

server = ServerThread()
server.start() # The server is now running
print "Listo servidor."
