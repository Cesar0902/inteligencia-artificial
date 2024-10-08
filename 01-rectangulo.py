class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)    

rectangulo = Rectangulo(5, 3)
print(f"Área: {rectangulo.area()}")
print(f"Perimetro: {rectangulo.perimetro()}")