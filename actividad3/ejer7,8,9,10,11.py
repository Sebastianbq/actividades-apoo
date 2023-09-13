class Cuenta_bancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar (self,deposito):
        self.balance += deposito
        print(f"se deposito {deposito} a la cuenta, saldo: {self.balance}")
    
    def retiro (self,retiro):
        if retiro <= self.balance:
            self.balance -= retiro
            print(f"se retiro {retiro} de la cuenta, saldo:  {self.balance}")
        else:
            print("saldo insuficiente")
        
    def aplicar_cuota_manejo(self):
        cuota= self.balance * 0.2
        self.balance -= cuota
        print("se aplico la cuota de manejo del 2%, el saldo es:",self.balance)
        return cuota
    
    def mostrar_detalles (self):
        print(f"numero de cuenta {self.numero_cuenta} propietarios {self.propietarios} y balance {self.balance}" )
        
propietarios = ["lius", "andrea"] 
cuenta1 = Cuenta_bancaria(100, propietarios, 1000)
cuenta1.depositar(100)
cuenta1.retiro(500)
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()
            
        