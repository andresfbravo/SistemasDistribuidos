import socket

#client example
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1024))
n1 = raw_input ( "Type in the operation number; 1 + ; 2 - ; 3 * ; 4 / ; 5 pow ; 6 sqrt: ; 7 log")
n2 = raw_input ( "Type in the first number:" )
n3 = raw_input ( "Type in the second number:")
client_socket . send (n1 + " " + n2 + " " + n3)
data = client_socket.recv(1024)
print 'Result: ' + data
client_socket . close ()
