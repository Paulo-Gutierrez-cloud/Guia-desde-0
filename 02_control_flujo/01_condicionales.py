# 01_condicionales.py
# Tomando decisiones con IF, ELIF y ELSE

# Los programas no siempre siguen una línea recta.
# A veces necesitan tomar decisiones basadas en condiciones.

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes votar y conducir.")
elif edad >= 13:
    print("Eres un adolescente.")
else:
    print("Eres un niño.")

print("Fin del programa.")

# --- EXPLICACIÓN ---
# if (si): Evalúa una condición. Si es True, ejecuta el bloque identado.
# elif (si no, si): Se evalúa si el 'if' anterior fue False.
# else (si no): Se ejecuta si ninguna de las condiciones anteriores fue True.

# --- EJERCICIO ---
# Vamos a crear un evaluador de notas.
# 1. Pide al usuario que ingrese una nota del 0 al 100.
# 2. Si la nota es mayor o igual a 90, imprime "Excelente".
# 3. Si la nota es mayor o igual a 70 (y menor que 90), imprime "Aprobado".
# 4. Si la nota es menor a 70, imprime "Reprobado".
# 5. (Opcional) Si la nota es menor a 0 o mayor a 100, imprime "Nota inválida".

# Escribe tu código aquí abajo:

nota = int(input("ingrese su nota del 0 al 100: "))

if nota >= 90:
    print("Excelente")
elif nota >=70 and 90 > nota:
    print("Aprobado")
else: 
    print("Reprobado")
