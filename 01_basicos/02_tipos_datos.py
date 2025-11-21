# 02_tipos_datos.py
# Profundizando en los tipos de datos

# En el ejercicio anterior vimos:
# - String (str): Texto
# - Integer (int): Números enteros
# - Float (float): Números con decimales
# - Boolean (bool): Verdadero (True) o Falso (False)

# Podemos saber de qué tipo es una variable usando la función type()
numero = 10
texto = "10"

print("La variable 'numero' es de tipo:", type(numero))
print("La variable 'texto' es de tipo:", type(texto))

# --- CONVERSIÓN DE TIPOS (CASTING) ---
# A veces necesitamos convertir un tipo de dato a otro.

# De texto a número entero
numero_desde_texto = int(texto)
print("Ahora 'numero_desde_texto' es:", numero_desde_texto, "y su tipo es:", type(numero_desde_texto))

# De número a texto
texto_desde_numero = str(numero)
print("Ahora 'texto_desde_numero' es:", texto_desde_numero, "y su tipo es:", type(texto_desde_numero))

# --- EJERCICIO ---
# 1. Crea una variable llamada 'precio' con el valor 50.5 (float)
# 2. Convierte 'precio' a un número entero (int) y guárdalo en una variable llamada 'precio_entero'.
# 3. Imprime el valor de 'precio_entero' (¿Qué pasó con el decimal?)
# 4. Crea una variable 'edad_texto' con el valor "25" (string).
# 5. Súmale 5 a 'edad_texto'. (Pista: Primero tienes que convertirlo a int, luego sumar, y luego imprimir).

# Escribe tu código aquí abajo:

precio = 50.5
precio_entero = int(precio)
print("El precio es:", precio_entero)

edad_texto = "25"
edad = int(edad_texto)
edad = edad + 5
print("La edad es:", edad)
