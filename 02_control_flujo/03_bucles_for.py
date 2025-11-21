# 03_bucles_for.py
# Iterando con FOR (Para)

# El bucle FOR es ideal cuando sabemos cuántas veces queremos repetir algo
# o cuando queremos recorrer una colección de cosas.

# 1. Usando range()
print("--- Contando del 0 al 4 ---")
for i in range(5): # range(5) genera números del 0 al 4
    print(i)

print("\n--- Contando del 1 al 5 ---")
for i in range(1, 6): # range(inicio, fin) -> El fin no se incluye
    print(i)

# 2. Recorriendo texto
print("\n--- Deletreando ---")
texto = "Python"
for letra in texto:
    print(letra)

# --- EJERCICIO ---
# Vamos a crear la tabla de multiplicar de un número.
# 1. Pide al usuario un número entero (ej: 5).
# 2. Usa un bucle FOR y range() para iterar del 1 al 10.
# 3. En cada vuelta, imprime la multiplicación.
#    Ejemplo: "5 x 1 = 5", "5 x 2 = 10", etc.

# Escribe tu código aquí abajo:

numero = int(input("ingrese un numero: "))
for i in range (1, 11):
    print(f"el resultado de {numero} * {i} = {numero * i}")
