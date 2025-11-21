# 01_listas.py
# Organizando datos con LISTAS

# Una lista es una colección ordenada de elementos.
# Se escriben entre corchetes [] y separados por comas.

frutas = ["Manzana", "Banana", "Naranja"]
print("Lista de frutas:", frutas)

# 1. Acceder a elementos
# En Python, el primer elemento es el índice 0.
print("La primera fruta es:", frutas[0])
print("La segunda fruta es:", frutas[1])

# 2. Agregar elementos (append)
frutas.append("Uva")
print("Lista después de agregar Uva:", frutas)

# 3. Eliminar elementos (remove)
frutas.remove("Banana")
print("Lista después de eliminar Banana:", frutas)

# 4. Saber cuántos elementos hay (len)
cantidad = len(frutas)
print(f"Hay {cantidad} frutas en la lista.")

# --- EJERCICIO ---
# Vamos a crear una lista de compras.
# 1. Crea una lista vacía llamada 'compras'. (Pista: compras = [])
# 2. Pide al usuario que ingrese 3 cosas para comprar (usa input() y append() tres veces).
#    O puedes usar un bucle for range(3) para pedirlo 3 veces, ¡tú eliges!
# 3. Imprime la lista completa.
# 4. Imprime el mensaje: "Tengo que comprar [X] cosas", donde [X] es la cantidad de elementos.

# Escribe tu código aquí abajo:
