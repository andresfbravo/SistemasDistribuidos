import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

print "Digite dos numeros"
Numero1=raw_input()
Numero2=raw_input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(Numero1)
data = s.recv(BUFFER_SIZE)
s.send(Numero2)
data = s.recv(BUFFER_SIZE)
s.close()

print "La suma es:", data