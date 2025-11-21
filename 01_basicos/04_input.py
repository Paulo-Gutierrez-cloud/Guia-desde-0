# 04_input.py
# Interactuando con el usuario

# Hasta ahora, los valores estaban fijos en el código.
# Con la función input(), podemos pedirle datos al usuario.

print("--- Ejemplo de Input ---")
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre, "¡Qué bueno verte!")

# IMPORTANTE: input() SIEMPRE devuelve un texto (string).
# Si queremos usar números, tenemos que convertirlo (castearlo).

edad_texto = input("¿Cuántos años tienes? ")
edad_numero = int(edad_texto) # Convertimos a entero

anio_nacimiento = 2025 - edad_numero
print("Entonces naciste aproximadamente en:", anio_nacimiento)

# --- EJERCICIO ---
# Vamos a crear una calculadora de propinas simple.
# 1. Pide al usuario el total de la cuenta (puede tener decimales, usa float).
# 2. Pide al usuario el porcentaje de propina que quiere dejar (ej: 10, 15, 20).
# 3. Calcula el monto de la propina (total * porcentaje / 100).
# 4. Calcula el total a pagar (total + propina).
# 5. Imprime un mensaje final con el monto de la propina y el total a pagar.

# Escribe tu código aquí abajo:

inicio = input("¿Cuánto es el total de la cuenta? ")
porcentaje = input("¿Cuánto porcentaje de propina quieres dejar? ")
propina = float(inicio) * float(porcentaje) / 100
total = float(inicio) + propina
print("El total a pagar es: ", total)