class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 == 0:
            return "No se puede dividir por 0"
        return self.num1 / self.num2

print("Calculadora")

num1 = None
num2 = None

while True:
    try:
        if num1 == None:
            num1 = float(input("Ingrese el primer número: "))
        
        num2 = float(input("Ingrese el segundo número: "))
        
        break
    except ValueError:
        print("Por favor, ingrese un número válido")

calculadora = Calculadora(num1, num2)

print(f"  {num1} + {num2} = {calculadora.sumar()}")
print(f"  {num1} - {num2} = {calculadora.restar()}")
print(f"  {num1} * {num2} = {calculadora.multiplicar()}")
print(f"  {num1} / {num2} = {calculadora.dividir()}")