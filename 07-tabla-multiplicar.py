while True:
    try:
        numero = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Ingrese un número entero")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")