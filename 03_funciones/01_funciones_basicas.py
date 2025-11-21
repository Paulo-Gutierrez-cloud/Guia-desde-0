# 01_funciones_basicas.py
# Creando nuestras propias herramientas: FUNCIONES

# Una función es un bloque de código reutilizable.
# En lugar de escribir el mismo código muchas veces, lo definimos una vez y lo llamamos cuando queramos.

# Definición de una función simple
def saludar():
    print("¡Hola! Bienvenido al curso de Python.")

# Llamada a la función
print("--- Llamando a la función ---")
saludar()

# Función con parámetros (información que recibe)
def saludar_persona(nombre):
    print(f"Hola, {nombre}. ¡Gusto en verte!")

print("\n--- Llamando a la función con parámetros ---")
saludar_persona("Paulo")
saludar_persona("Ana")

# Función que devuelve un valor (return)
def sumar(a, b):
    resultado = a + b
    return resultado

print("\n--- Usando el valor de retorno ---")
total = sumar(5, 3)
print(f"La suma es: {total}")

# --- EJERCICIO ---
# 1. Crea una función llamada 'calcular_area_rectangulo'.
# 2. Debe recibir dos parámetros: 'base' y 'altura'.
# 3. Debe calcular el área (base * altura) y RETORNAR el resultado.
# 4. Fuera de la función, pide al usuario la base y la altura.
# 5. Llama a tu función y guarda el resultado en una variable.
# 6. Imprime el resultado final.

# Escribe tu código aquí abajo:

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

base = int(input("ingrese base del rectangulo: "))
altura = int(input("ingrese altura del rectangulo: "))

area = calcular_area_rectangulo(base, altura)
print(f"el area del rectangulo es: {area}")