def contar_vocales(frase):
    frase = frase.lower()
    vocales = 'aeiou'
    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1
    
    return contador

frase = input("Ingrese una frase: ")
print(f"La frase tiene {contar_vocales(frase)} vocales.")