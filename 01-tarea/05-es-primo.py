def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
if es_primo(n):
    print(f"{n} es primo")

# numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in numeros:
#     if es_primo(n):
#         print(f"{n} es primo")
#     else:
#         print(f"{n} no es primo")