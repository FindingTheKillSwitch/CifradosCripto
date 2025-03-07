import random

# Tabla de frecuencias completa en español con numeros del 1 al 75
tabla_frecuencias = {
    "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "A": [11, 12, 13, 14, 15, 16, 17, 18, 19],
    "O": [20, 21, 22, 23, 24, 25],
    "L": [26, 27, 28, 29, 30, 31],
    "S": [32, 33, 34, 35, 36, 37],
    "N": [38, 39, 40, 41, 42, 43],
    "D": [44, 45, 46, 47, 48],
    "R": [49, 50, 51, 52, 53],
    "U": [54, 55, 56, 57],
    "I": [58, 59, 60, 61],
    "T": [62, 63, 64],
    "C": [65, 66, 67],
    "M": [68, 69],
    "P": [70, 71],
    "B": [72],
    "V": [73],
    "Q": [74],
    "G": [75],
    "H": [76],
    "F": [77],
    "Y": [78],
    "Z": [79],
    "J": [80],
    "Ñ": [81],
    "X": [82],
    "K": [83],
    "W": [84]
}

# Generar la tabla inversa para descifrar
tabla_inversa = {num: letra for letra, numeros in tabla_frecuencias.items() for num in numeros}

def cifrar(texto): #Cifrado Homofonico
    texto = texto.upper()
    cifrado = []
    
    for letra in texto:
        if letra in tabla_frecuencias:
            cifrado.append(str(random.choice(tabla_frecuencias[letra])))  # Se elige la frecuencia aleatoriamente de acuerdo a las opcioens en la tabla
        else:
            cifrado.append(letra)

    return " ".join(cifrado)

def descifrar(texto_cifrado):#Descifrado Homofonico
    numeros = texto_cifrado.split()
    descifrado = ""

    for num in numeros:
        if num.isdigit() and int(num) in tabla_inversa:
            descifrado += tabla_inversa[int(num)]
        else:
            descifrado += num

    return descifrado

#Se escribe el mensaje a cifrar
mensaje = "Hola profe de Criptografia"
cifrado = cifrar(mensaje)
descifrado = descifrar(cifrado)

print(f"Texto original: {mensaje}")
print(f"Texto cifrado: {cifrado}")
print(f"Texto descifrado: {descifrado}")
