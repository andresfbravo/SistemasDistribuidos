import socket
#servidor andres reinosa
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data2, addr = sock.recvfrom(1024)
    a = int(data)
    b = int(data2)
    suma = a + b
    
    sock.sendto(str(suma),(addr[0],addr[1]))
    
    
    
    
    
    
    
