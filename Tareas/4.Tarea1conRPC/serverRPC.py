from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9999),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

#registro funciones predeterminadas de python
#server.register_function(pow)

class MyFuncs:
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

server.register_instance(MyFuncs())
print "servidorCorriendo"
# Correr servidor indefinidamente
server.serve_forever()
