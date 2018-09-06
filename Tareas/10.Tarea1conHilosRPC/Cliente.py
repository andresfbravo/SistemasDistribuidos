from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
from Scanner import Scanner

def mekeOperation(sc,s):
	if((sc).getOperation()=="+"):
		return s.add(sc.getNro1(),sc.getNro2())
	elif((sc).getOperation()=="-"):
		return s.sub(sc.getNro1(),sc.getNro2())
	elif((sc).getOperation()=="*"):
		return s.mul(sc.getNro1(),sc.getNro2())
	elif((sc).getOperation()=="/"):
		return s.div(sc.getNro1(),sc.getNro2())
	elif((sc).getOperation()=="pow"):
		return s.rad(sc.getNro1(),sc.getNro2())
	elif((sc).getOperation()=="rad"):
		return s.pow(sc.getNro1(),sc.getNro2())
	elif((sc).getOperation()=="log"):
		return s.log(sc.getNro1(),sc.getNro2())

class ClientThread(threading.Thread):
    def __init__(self):
    	self.sc=Scanner()
    	threading.Thread.__init__(self)
    	self.s = xmlrpclib.ServerProxy('http://localhost:9992')



    def toString(self):
    	x= "La operacion "+str(self.sc.getNro1())+" "+self.sc.getOperation()+" "+str(self.sc.getNro2())+" = "+str(mekeOperation(self.sc,self.s))
    	return x

    def run(self):
		#time.sleep(3)
		print "Llamada cliente1 "
		print self.toString()
		#print  "La operacion ",self.sc.getNro1()," ",self.sc.getOperation()," ",self.sc.getNro2()," = ",mekeOperation(self.sc,self.s)
		#print "Esto da: ",self.s.div(5,2)  # Returns 5//2 = 2
		#print self.s.add(7,2)
"""
class ClientThread2(threading.Thread):
    def __init__(self):
		threading.Thread.__init__(self)
		self.s = xmlrpclib.ServerProxy('http://localhost:9998')

    def run(self):
		#time.sleep(3)
		print "Llamada cliente2 "
		print "Fsto da: ",self.s.add(7,2)
		#print self.s.div(5,2)  # Returns 5//2 = 2
"""
client = ClientThread()
#client2 = ClientThread2()
client.start() # The server is now running
#client2.start()