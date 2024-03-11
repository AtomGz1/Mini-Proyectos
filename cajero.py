class Cajero:
    monto = 0
    print("BIENVENIDO A SU CAJERO AUTOMATICO")
    def operaciones(self):
        self.opcion = int(input('''
        ------------------------------------------
        INDIQUE LA OPERACION A REALIZAR...
        1. CONSULTAR BALANCE
        2. DEPOSITO
        3. RETIRO DE EFECTIVO
        4. SALIR'''))
        self.control = 0
        while self.control == 0:
            if self.opcion == 1:
                self.consultar_balance()
            elif self.opcion == 2:
                self.depositar()
            elif self.opcion == 3:
                self.retirar()
            elif self.opcion == 4:
                self.control = 1
                self.salir()
            else:
                print("OPCION NO VALIDA, INTENTE DE NUEVO")
                self.operaciones()
        
    def consultar_balance(self):
        print("SU BALANCE DISPONIBLE ES DE: ", self.monto)
        print("DESEA REALIZAR OTRA OPERACION?")
        self.operaciones()

    def depositar(self):
        self.deposito = int(input("INDIQUE LA CANTIDAD A DEPOSITAR: "))
        self.monto = self.monto + self.deposito
        self.consultar_balance()

    def retirar(self):
        self.retiro = int(input("INDIQUE LA CANTIDAD A RETIRAR: "))
        self.control = 0
        while self.control == 0:
            if self.retiro > self.monto:
               print("NO POSEE SALDO SUFICIENTE, INGRESE OTRO MONTO")
               self.retiro = int(input("INDIQUE LA CANTIDAD A RETIRAR: "))
            elif self.retiro <= self.monto:
               self.monto = self.monto - self.retiro
               self.control = 1
               print("USTED RETIRO: ", self.retiro)
               self.consultar_balance()

    def salir(self):
        print("----------------------------------")
        print("GRACIAS POR USAR NUESTRO SERVICIO")
        print("----------------------------------")

ejecucion = Cajero()
ejecucion.operaciones()    
