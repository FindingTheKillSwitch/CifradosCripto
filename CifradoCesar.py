def cifradoCesar(mensaje, desplazamiento, alfabeto):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter in alfabeto:
            indice_original = alfabeto.index(caracter)
            indice_cifrado = (indice_original + desplazamiento) % len(alfabeto
            mensaje_cifrado += alfabeto[indice_cifrado]
        else:
            mensaje_cifrado += caracter
    return mensaje_cifrado

def descifradoCesar(mensaje_cifrado, desplazamiento, alfabeto):
    mensaje_descifrado = ""
    for caracter in mensaje_cifrado:
        if caracter in alfabeto:
            indice_cifrado = alfabeto.index(caracter)
            indice_descifrado = (indice_cifrado - desplazamiento) % len(alfabeto)
            mensaje_descifrado += alfabeto[indice_descifrado]
        else:
            mensaje_descifrado += caracter
    return mensaje_descifrado

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
mensaje = "Mensaje"
desplazamiento = 3

mensaje_cifrado = cifradoCesar(mensaje, desplazamiento, alfabeto)
print(f"Mensaje cifrado: {mensaje_cifrado}")

mensaje_descifrado = descifradoCesar(mensaje_cifrado, desplazamiento, alfabeto)
print(f"Mensaje descifrado: {mensaje_descifrado}")
