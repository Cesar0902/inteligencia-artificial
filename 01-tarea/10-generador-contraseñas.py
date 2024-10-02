from random import choice, randint, shuffle

patron = ['M', 'm', 'n', 's']
contraseña = ""

patron += [choice(patron) for _ in range(4)]
shuffle(patron)

for letra in patron:
  match letra:
    case 'M':
      contraseña += chr(randint(65, 90))
    case 'm':
      contraseña += chr(randint(97, 122))
    case 'n':
      contraseña += chr(randint(48, 57))
    case 's':
      contraseña += chr(randint(33, 47))

print(f"Contraseña generada es: {contraseña}")