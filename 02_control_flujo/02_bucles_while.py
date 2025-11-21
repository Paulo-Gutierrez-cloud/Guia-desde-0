# 02_bucles_while.py
# Repitiendo acciones con WHILE (Mientras)

# A veces queremos que un código se repita varias veces
# mientras se cumpla una condición.

contador = 1

print("--- Contando hasta 5 ---")
while contador <= 5:
    print("Contador:", contador)
    contador = contador + 1 # Importante: aumentar el contador para no crear un bucle infinito

print("¡Fin del conteo!")

# --- BREAK (Romper) ---
# Podemos detener un bucle antes de tiempo usando 'break'.

print("\n--- Buscando el número 3 ---")
numero = 1
while numero <= 10:
    print("Probando número:", numero)
    if numero == 3:
        print("¡Lo encontré! Deteniendo búsqueda.")
        break # Sale del bucle inmediatamente
    numero = numero + 1

# --- EJERCICIO ---
# Vamos a crear un juego de "Adivina el número".
# 1. Define una variable 'numero_secreto' con un valor del 1 al 10 (ej: 7).
# 2. Pide al usuario que adivine el número usando input() dentro de un bucle while.
# 3. El bucle debe repetirse MIENTRAS el usuario NO adivine el número.
# 4. Si adivina, imprime "¡Correcto!" y el programa termina.
# 5. (Opcional) Si falla, dale una pista (ej: "Es más alto" o "Es más bajo").

# Pista: Necesitarás inicializar la variable de la adivinanza antes del bucle
# o usar un 'while True' con un 'break' cuando adivine.

# Escribe tu código aquí abajo:

numero_secreto = 6
usuario = int(input("adivina el numero: "))
while usuario != numero_secreto:
    print("intentalo de nuevo")
    if usuario < numero_secreto:
        print("es mas alto")
    else:
        print("es mas bajo")
    usuario = int(input("adivina el numero: "))
if usuario == numero_secreto:
    print("correcto")
