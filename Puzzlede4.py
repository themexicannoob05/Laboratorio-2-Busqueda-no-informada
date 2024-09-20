from collections import deque as mi_pila

# Función para generar los movimientos posibles (intercambios en este caso)
def obtener_movimientos(posicion_actual):
    movimientos = []
    # Intercambiar dos elementos adyacentes
    for i in range(len(posicion_actual) - 1):
        nuevo_estado = list(posicion_actual)  # Crear copia del estado actual
        nuevo_estado[i], nuevo_estado[i + 1] = nuevo_estado[i + 1], nuevo_estado[i]
        movimientos.append(tuple(nuevo_estado))
    return movimientos

# Función DFS para resolver el puzzle
def dfs(puzzle_inicial, objetivo):
    pila = mi_pila()  # Crear la pila
    pila.append(puzzle_inicial)  # Agregar el estado inicial
    visitados = set()  # Mantener un registro de estados ya visitados
    
    while pila:
        estado_actual = pila.pop()  # Obtener el estado actual
        print(f"Visitando estado: {estado_actual}")
        
        if estado_actual == objetivo:  # Si encontramos la solución
            print("¡Puzzle resuelto!")
            return True
        
        visitados.add(estado_actual)  # Marcar como visitado
        
        # Generar y explorar nuevos movimientos
        for nuevo_estado in obtener_movimientos(estado_actual):
            if nuevo_estado not in visitados:  # Evitar estados repetidos
                pila.append(nuevo_estado)
    
    print("No se encontró solución.")
    return False

# Estado inicial y estado objetivo
estado_inicial = (2, 1, 3, 4)
estado_objetivo = (1, 2, 3, 4)

# Resolver el puzzle
dfs(estado_inicial, estado_objetivo)
