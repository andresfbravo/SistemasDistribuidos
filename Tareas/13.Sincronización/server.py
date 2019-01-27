import socket
import sys
import thread

class grupos():
        def constructor(self):
                self.grupo = {}
                self.mensajes = {}
        def crear_grupo(self,puerto,nombre):
                self.grupo[nombre] = [puerto]
                self.mensajes[nombre] = 'No hay mensajes'
                return 'grupo creado'
        def unirse_agrupo(self,puerto,nombre):
                if self.grupo:
                        self.grupo[nombre].append(puerto)
                        return 'Usted se ha unido al grupo satisfactoriamente'
                else:
                        return 'No existe ningun grupo'
        def nuevo_mensaje(self, nombre, mensaje):
        		self.mensajes[nombre] = mensaje
        def get_grupos(self):
                return self.grupo
        def get_mensajes(self):
        		return self.mensajes
                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9882))
s.listen(10)


groups = grupos()
groups.constructor()
j = ''
def connection(sc, addr, rc):
	
	while True:
		messen = 'Usted tiene nuevos mensajes:\n'
		print "ENTRO!!!!!"
		enviar = 0
		entro = False
		numero1 = sc.recv(1024)
		a ,b , c= numero1.split(' ')
		if int(a) == 1:
			j = groups.crear_grupo(int(b), c)   
			sc.send(str(j))    
		elif int(a)== 2:
			cadena = ''
			cont = 1
			for i in groups.get_grupos():
				print i, 'jajaja'
				cadena += str(cont) + '. '+ i +'\n'
				cont += 1
			sc.send(cadena)
			numero1=sc.recv(1024)
			a ,b , c= numero1.split(' ')
			cadena = ''
			cont = 1
			for i in groups.get_grupos():
				if cont == int(c):
					cadena = i
				cont += 1
			print c , 'jejeje'
			j = groups.unirse_agrupo(int(b), cadena)
			sc.send(str(j))
		elif int(a) == 3:
			n = groups.get_grupos()
			for i in n:
				if int(b) in n[i]:
					groups.nuevo_mensaje(i,c)
		n = groups.get_grupos()
		m = groups.get_mensajes()
		for i in n:
			if int(b) in n[i]:
				if m[i] != 'No hay mensajes':
					entro = True
					messen += m[i]+'\n'
		if entro == False:
			messen = 'No hay mensajes'
		rc.send(messen)


print "respondiendo..."

while True:
	sc, addr = s.accept()
	r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	numero1 = sc.recv(1024)
	a ,b , c= numero1.split(' ')
	r.bind(('', int(b)))
	r.listen(10)
	print 'llego aca'
	rc, puerto = r.accept()
	print "recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1])
	print "\n"
	thread.start_new_thread(connection,(sc,addr,rc))
	print 'interesting'
    
sc.close()
s.close()
rc.close()
r.close()


