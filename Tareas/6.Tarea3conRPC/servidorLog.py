from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9992),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def log(self,numero1,numero2):
		return math.log(int(numero1),int(numero2))

server.register_instance(MyFuncs())
print "servidorLogCorriendo"
# Correr servidor indefinidamente
server.serve_forever()