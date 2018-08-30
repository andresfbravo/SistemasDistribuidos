from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib

#instancio un objeto y conecto el servidor a donde se va a conectar
"""
servidorSuma = xmlrpclib.ServerProxy('http://localhost:9998')
servidorSub = xmlrpclib.ServerProxy('http://localhost:9997')
servidorMul = xmlrpclib.ServerProxy('http://localhost:9996')
servidorDiv = xmlrpclib.ServerProxy('http://localhost:9995')
servidorRad = xmlrpclib.ServerProxy('http://localhost:9994')
servidorPow = xmlrpclib.ServerProxy('http://localhost:9993')
servidorLog = xmlrpclib.ServerProxy('http://localhost:9992')
"""
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9999),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def redireccionar(self,datos):
		self.valores=datos.split("@")
		self.operacion=self.valores[2]
		#print self.valores[0],self.valores[1],self.valores[2]
		if(self.operacion=="+"):
			#self.operacion="+"
			#print servidorSuma.add(self.valores[0],self.valores[1])
			return 'http://localhost:9998'
		elif(self.operacion=="-"):
			#print servidorSub.sub(self.valores[0],self.valores[1])
			return 'http://localhost:9997'
		elif(self.operacion=="x"):
			#print servidorMul.mul(self.valores[0],self.valores[1])
			return 'http://localhost:9996'
		elif(self.operacion=="/"):
			#print servidorDiv.div(self.valores[0],self.valores[1])
			return 'http://localhost:9995'
		elif(self.operacion=="rad"):
			#print servidorRad.rad(self.valores[0],self.valores[1])
			return 'http://localhost:9994'
		elif(self.operacion=="pow"):
			#print servidorPow.pow(self.valores[0],self.valores[1])
			return 'http://localhost:9993'
		elif(self.operacion=="log"):
			#print servidorLog.log(self.valores[0],self.valores[1])
			return 'http://localhost:9992'
		

server.register_instance(MyFuncs())
print "servidorIntermedioCorriendo"
# Correr servidor indefinidamente
server.serve_forever()