def dfs_maze(maze, start, end):
    pilita = [(start, [start])]  # La pila contiene tuplas con la posición actual y el camino recorrido
    visited = set()

    while pilita:
        (current, path) = pilita.pop()

        if current == end:
            return path  # Se encontró el final, devolver el camino

        if current in visited:
            continue

        visited.add(current)

        # Obtener las coordenadas de vecinos válidos (movimientos posibles: arriba, abajo, izquierda, derecha)
        neighbors = get_neighbors(maze, current)

        for neighbor in neighbors:
            if neighbor not in visited:
                pilita.append((neighbor, path + [neighbor]))

    return None  # No se encontró una solución

def get_neighbors(maze, position):
    neighbors = []
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos: arriba, abajo, izquierda, derecha

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0:
            neighbors.append((r, c))

    return neighbors


# Ejemplo de uso para resolver el laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

start = (0, 1)
end = (3, 4)

solution = dfs_maze(maze, start, end)
print("Ruta encontrada en el laberinto:", solution)