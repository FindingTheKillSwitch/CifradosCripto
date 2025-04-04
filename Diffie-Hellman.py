import sympy

print("Serapio Hernandez Alexis Arturo\n")
print("Hola! Este es el algoritmo de intercambio de llaves 'Diffie-Hellman'")
print("\nEjemplos de números primos que puedes usar:")
num_primos = [23, 47, 101, 199, 499, 997]
print(num_primos)

print("\nEjemplos de base generadora valida:")
num_generadora = [2, 3, 5, 7, 11]
print(num_generadora)

# Paso 1: Se declara un número primo público y la base generadora
primo = int(input("\nIngresa un número primo: "))
generadora = int(input("Ingresa una base generadora: "))

if not sympy.isprime(primo):
    print("Error: el número que ingresaste no es un número primo")
    exit()

if not (2 <= generadora < primo):
    print("Error: La base generadora debe ser mayor o igual a 2 y menor que el número primo ingresado")
    exit()

# Paso 2: Cada usuario ingresa su clave privada
llave_privada_alice = int(input(f"Ingresa la clave privada de Alice (entre 1 y {primo-2}): "))
llave_privada_bob = int(input(f"Ingresa la clave privada de Bob (entre 1 y {primo-2}): "))

if not (1 <= llave_privada_alice <= primo-2 and 1 <= llave_privada_bob <= primo-2):
    print("Error: La clave privada debe estar entre 1 y el numero primo-2")
    exit()

# Paso 3: Se generan las llaves públicas
llave_publica_alice = pow(generadora, llave_privada_alice, primo)  # A = g^a mod p
llave_publica_bob = pow(generadora, llave_privada_bob, primo)  # B = g^b mod p

# Paso 4: Se genera la clave compartida
llave_compartida_alice = pow(llave_publica_bob, llave_privada_alice, primo)  # B^a mod p
llave_compartida_bob   = pow(llave_publica_alice, llave_privada_bob, primo)  # A^b mod p

print(f"\nIngresaste:")
print(f"Número primo público: {primo}")
print(f"Base generadora pública: {generadora}")
print(f"Clave privada de Alice: {llave_privada_alice}")
print(f"Clave privada de Bob: {llave_privada_bob}")

print(f"\nClaves públicas generadas:")
print(f"Clave pública de Alice: {llave_publica_alice}")
print(f"Clave pública de Bob: {llave_publica_bob}")

print(f"\nClaves compartidas calculadas:")
print(f"Clave compartida de Alice: {llave_compartida_alice}")
print(f"Clave compartida de Bob: {llave_compartida_bob}")

# Si ambas claves son iguales, el intercambio ha sido exitoso
if llave_compartida_alice == llave_compartida_bob:
    print("\nIntercambio exitoso: Ambas partes tienen la misma clave secreta.")
else:
    print("\nError: Las claves compartidas no coinciden.")
