from operator import length_hint
# Tabla de permutación inicial (PI)
PI = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

def permutar(bits, tabla):
    return [bits[i - 1] for i in tabla]

# Ejemplo: entrada de 64 bits como lista de 0s y 1s
def string_a_bitlist(s):
    return [int(b) for char in s for b in format(ord(char), '08b')]

def bitlist_a_string(b):
    return ''.join(chr(int(''.join(map(str, b[i:i+8])), 2)) for i in range(0, len(b), 8))

# Probamos
mensaje = "CRIPTO12"  # 8 caracteres = 64 bits
print("Texto Original: ", mensaje)
key = "12345678"
print("Llave: ", key)

bits = string_a_bitlist(mensaje)

print("Bits originales:", bits)
print(length_hint(bits))
permutados = permutar(bits, PI)
print("Bits permutados:", permutados)
print(length_hint(permutados))

#Paso 2
def dividir_en_dos(bits):
    mitad = len(bits) // 2
    return bits[:mitad], bits[mitad:]

# PC-1: Permutación para reducir clave de 64 bits a 56 bits
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
]

# PC-2: Para comprimir de 56 a 48 bits
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Número de rotaciones por ronda
ROTACIONES = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# Rotar Izquierda
def rotar_izquierda(bits, n):
    return bits[n:] + bits[:n]

# Generar Subclaves

def generar_subkeys(key_64bits):
    # Aplicamos PC-1 para obtener 56 bits
    key_56 = permutar(key_64bits, PC1)
    # Dividimos en C y D
    C = key_56[:28]
    D = key_56[28:]
    
    subkeys = []
    
    for rotacion in ROTACIONES:
        C = rotar_izquierda(C, rotacion)
        D = rotar_izquierda(D, rotacion)
        CD = C + D
        subkey = permutar(CD, PC2)
        subkeys.append(subkey)
    return subkeys

clave = "12345678"  # 8 caracteres = 64 bits
clave_bits = string_a_bitlist(clave)
subclaves = generar_subkeys(clave_bits)

print("Subclave 1:", subclaves[0])
print(length_hint(subclaves[0]))
print("Subclave 16:", subclaves[-1])
print(length_hint(subclaves[-1]))

#Tabla de Expansion

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

CAJAS_S = [
    # S1
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    ],
    # S2
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    ],
    # S3
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    ],
    # S4
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    ],
    # S5
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    ],
    # S6
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    ],
    # S7
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    ],
    # S8
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
    ]
]


#Permutacion Final

PF = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

def sustitucion_cajas_s(bits48):
    output = []
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        fila = (block[0] << 1) + block[5]
        columna = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
        v = CAJAS_S[i][fila][columna]
        output += [int(x) for x in format(v, '04b')]
    return output

#Funcion F

def f(R, K):
    # Expansión de R (32 → 48)
    expansion_de_R = permutar(R, E)

    # XOR con subclave
    resultado_xor = [r ^ k for r, k in zip(expansion_de_R, K)]

    # Sustitución con S-boxes
    salida_cajas = sustitucion_cajas_s(resultado_xor)

    # Permutación final
    return permutar(salida_cajas, PF)

#Se realizan las 16 rondas de DES

def rondas_DES(L0, R0, subkeys):
    L, R = L0, R0
    for i in range(16):
        L_siguiente = R
        R_siguente = [l ^ r for l, r in zip(L, f(R, subkeys[i]))]
        L, R = L_siguiente, R_siguente
    return R, L  # Ojo: se invierten al final

#Se permuta finalmente

PI_inversa = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,  49, 17, 57, 25
]

def permutacion_final(bits):
    return permutar(bits, PI_inversa)
  
#Funcion principal para encriptar usando DES

def encriptar_DES(plaintext, key):
    # Convertir texto a bits
    bits_texto_plano= string_a_bitlist(plaintext)
    key_bits = string_a_bitlist(key)

    # Paso 1: Permutación inicial
    inicial = permutar(bits_texto_plano, PI)

    # Paso 2: Dividir en L0 y R0
    L0, R0 = dividir_en_dos(inicial)

    # Paso 3: Subclaves
    subkeys = generar_subkeys(key_bits)

    # Paso 4: Rondas de Feistel
    R16, L16 = rondas_DES(L0, R0, subkeys)

    # Paso 5: Permutación final
    bits_finales = permutacion_final(R16 + L16)

    return bits_finales

# Asegúrate de que ambas entradas son de 8 caracteres
if len(mensaje) != 8 or len(key) != 8:
    raise ValueError("El texto y la llave deben tener exactamente 8 caracteres (64 bits).")

cifrar_bits = encriptar_DES(mensaje, key)

# Mostrar salida como bits
print("Texto cifrado (bits):")
print(''.join(str(b) for b in cifrar_bits))

# Mostrar salida como hexadecimal (más legible)
cifrar_bytes = [int(''.join(str(bit) for bit in cifrar_bits[i:i+8]), 2) for i in range(0, 64, 8)]
cifrar_hex = ''.join(f'{b:02X}' for b in cifrar_bytes)
print("Texto cifrado (hex):", cifrar_hex)

#Rutina de Desencriptacion

def desencriptar_DES(ciphertext_bits, key):
    # Convertimos la clave a bits
    key_bits = string_a_bitlist(key)

    # Paso 1: Permutación inicial
    inicial = permutar(ciphertext_bits, PI)

    # Paso 2: Dividir en L0 y R0
    L0, R0 = dividir_en_dos(inicial)

    # Paso 3: Subclaves en orden inverso
    subkeys = generar_subkeys(key_bits)[::-1]

    # Paso 4: Rondas de Feistel con subclaves inversas
    R16, L16 = rondas_DES(L0, R0, subkeys)

    # Paso 5: Permutación final inversa
    bits_finales = permutacion_final(R16 + L16)

    return bits_finales

# Desencriptar el resultado de cifrar
bits_descifrados = desencriptar_DES(cifrar_bits, key)
mensaje_descifrado = bitlist_a_string(bits_descifrados)

print("Texto descifrado:", mensaje_descifrado)

