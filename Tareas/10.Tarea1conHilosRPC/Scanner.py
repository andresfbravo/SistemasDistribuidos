


class Scanner:

    def __init__(self):

        self.operacion = self.ScanearOperacion()
        self.nro1 = self.ScanearNumero()
        self.nro2 = self.ScanearNumero()

    def getDataToSend(self):

        return self.nro1 + " " + self.nro2 + " " + self.operacion

    def getNro1(self):

        return int(self.nro1)


    def getNro2(self):

        return int(self.nro2)


    def getOperation(self):

        return self.operacion


    def ScanearOperacion(self):


        l = ['+', '-', '*', '/', 'pow', 'rad', 'log']
        opc = 0
        inrange = True
        while(inrange):
            #limpiar pantall
            print("limpiar pantalla")

            print("ESCOJA UNA OPERACION MATEMATICA: ")
            print("\t1. +")
            print("\t2. -")
            print("\t3. *")
            print("\t4. /")
            print("\t5. pow")
            print("\t6 .rad")
            print("\t7. log")

            try:
                opc = int(raw_input("Digite su opcion: "))
                inrange = not (0 < opc < 8)
            except Exception as e:
                pass


        return l[opc - 1]


    def ScanearNumero(self):

        while(True):
            #limpiar pantlla
            n = raw_input('Ingrese un numero: ')
            try:
                int(n)
                return n
            except Exception as e:
                print("Hubo un error, recuerde ingresar solo numeros.")
