def generar_clave(mensaje, clave):
    clave = list(clave)
    if len(clave) == len(mensaje):
        return "".join(clave)
    else:
        for i in range(len(mensaje) - len(clave)):
            clave.append(clave[i % len(clave)])
    return "".join(clave)

def cifrar_vigenere(mensaje, clave, alfabeto):
    mensaje_cifrado = ""
    clave = generar_clave(mensaje, clave)
    for i in range(len(mensaje)):
        if mensaje[i] in alfabeto:
            indice_mensaje = alfabeto.index(mensaje[i])
            indice_clave = alfabeto.index(clave[i])
            indice_cifrado = (indice_mensaje + indice_clave) % len(alfabeto)
            mensaje_cifrado += alfabeto[indice_cifrado]
        else:
            mensaje_cifrado += mensaje[i]
    return mensaje_cifrado

def descifrar_vigenere(mensaje_cifrado, clave, alfabeto):
    mensaje_descifrado = ""
    clave = generar_clave(mensaje_cifrado, clave)
    for i in range(len(mensaje_cifrado)):
        if mensaje_cifrado[i] in alfabeto:
            indice_cifrado = alfabeto.index(mensaje_cifrado[i])
            indice_clave = alfabeto.index(clave[i])
            indice_descifrado = (indice_cifrado - indice_clave) % len(alfabeto)
            mensaje_descifrado += alfabeto[indice_descifrado]
        else:
            mensaje_descifrado += mensaje_cifrado[i]
    return mensaje_descifrado

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
mensaje = "Mensaje"
clave = "Cripto"

mensaje_cifrado = cifrar_vigenere(mensaje, clave, alfabeto)
print(f"Mensaje cifrado: {mensaje_cifrado}")

mensaje_descifrado = descifrar_vigenere(mensaje_cifrado, clave, alfabeto)
print(f"Mensaje descifrado: {mensaje_descifrado}")
