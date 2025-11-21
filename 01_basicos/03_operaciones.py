# 03_operaciones.py
# Operaciones Matemáticas Básicas

# Python funciona como una calculadora potente.
a = 10
b = 3

print("Variables: a =", a, ", b =", b)

# Suma (+)
print("Suma:", a + b)

# Resta (-)
print("Resta:", a - b)

# Multiplicación (*)
print("Multiplicación:", a * b)

# División (/) - Siempre devuelve un float
print("División:", a / b)

# División Entera (//) - Devuelve solo la parte entera
print("División Entera:", a // b)

# Módulo (%) - Devuelve el resto de la división
print("Módulo (Resto):", a % b)

# Potencia (**) - a elevado a b
print("Potencia:", a ** b)

# --- EJERCICIO ---
# 1. Crea dos variables: 'base' con valor 5 y 'altura' con valor 10.
# 2. Calcula el área de un triángulo (base * altura / 2) y guárdalo en una variable 'area'.
# 3. Imprime el resultado con un mensaje: "El área del triángulo es: [resultado]"
# 4. Calcula el resto de dividir 17 entre 3 e imprímelo.

# Escribe tu código aquí abajo:

base = 5
altura = 10
area = (base * altura / 2)
print("el area del triangulo es:", area)

resto = 17 % 3
print("El resto de dividir 17 entre 3 es:", resto)