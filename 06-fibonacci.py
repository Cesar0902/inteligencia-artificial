def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while True:
    try:
        n = int(input("Ingrese el límite de la serie de Fibonacci: "))
        if n < 0:
            print("El número debe ser positivo")
        else:
            break
    except ValueError:
        print("Ingrese un número entero")

for i in range(n):
    if i < n-1:
        print(fibonacci(i), end=", ")
    else:
        print(fibonacci(i), end="\n")