class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: float):
        self.saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print('Fondos insuficientes')

    def mostrar_saldo(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo: ${self.saldo}')
        print('------------------------------')

cuenta = CuentaBancaria('Alice')
cuenta.mostrar_saldo()
cuenta.depositar(100)
cuenta.mostrar_saldo()
cuenta.retirar(50)
cuenta.mostrar_saldo()
cuenta.retirar(100)