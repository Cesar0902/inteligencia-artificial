from random import randint

numero = randint(1, 100)
intentos = 0

while True:
  intento = int(input("Adivina el número: "))
  intentos += 1
  if intento == numero:
    print(f"¡Adivinaste el número en {intentos} intentos!")
    break
  elif intento < numero:
    print("El número es mayor.")
  else:
    print("El número es menor.")