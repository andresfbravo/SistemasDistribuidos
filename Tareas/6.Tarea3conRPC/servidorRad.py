from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9994),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def rad(self,numero1,numero2):
		numero2=1/int(numero2)
		return pow(int(numero1),numero2)

server.register_instance(MyFuncs())
print "servidorRadCorriendo"
# Correr servidor indefinidamente
server.serve_forever()