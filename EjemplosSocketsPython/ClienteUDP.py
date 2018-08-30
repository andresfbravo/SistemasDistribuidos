import socket
#cliente andres reinosa

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
a = raw_input("Digite numero: ")
b = raw_input("Digite numero: ")

print "UDP TARGET IP:", UDP_IP
print "UDP TARGET PORT:", UDP_PORT
print "Enviando a y b:", a,"y", b

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(a,(UDP_IP,UDP_PORT))
sock.sendto(b,(UDP_IP,UDP_PORT))

suma , addr = sock.recvfrom(1024)
print "Received message lindo, and the sum is", suma
