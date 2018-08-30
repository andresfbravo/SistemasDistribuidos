'''
    Simple socket server using threads
'''
 
import socket
import sys
import thread
import math
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 1024 # Arbitrary non-privileged port
 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    serversocket.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
serversocket.listen(10)
print 'Socket now listening'

def handler(conn, addr):    
        data = conn . recv (1025)
#       reply = 'OK...' + data + ';'
        n1, n2, n3 = data . split ()

        if n1 == '1':
            n4 = float(n2) + float(n3)
        elif n1 == '2':
            n4 = float(n2) - float(n3)
        elif n1 == '3':
            n4 = float(n2) * float(n3)
        elif n1 == '4':
            n4 = float(n2) / float(n3)
        elif n1 == '5':
            n4 = pow(float(n2), float(n3))
        elif n1 == '6':
            #n4 = math . sqrt(float(n2))
            n4 = pow(float(n2), float(1/n3))
        elif n1 == '7':
            n4 = math.log(float(n2), float(n3))                        
        print n4
        reply = str(n4)
        conn.sendall(reply)

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = serversocket.accept()    
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    thread . start_new_thread (handler, (conn, addr))
    
     
s.close()
