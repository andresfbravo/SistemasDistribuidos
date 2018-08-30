from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9996),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def mul(self,numero1,numero2):
		return int(numero1) * int(numero2)

server.register_instance(MyFuncs())
print "servidorMulCorriendo"
# Correr servidor indefinidamente
server.serve_forever()