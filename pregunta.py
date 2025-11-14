
laberinto = [
    [1, 1, 1, 1, 99, 1, 1, 1, 0],   # 0 = Inicio (I)
    [1, 99, 99, 1, 99, 1, 99, 1, 1],
    [1, 1, 99, 1, 1, 1, 99, 1, 99],
    [99, 1, 1, 99, 99, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 1, 99, 99, 1, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 1, 99, 1, 2, 99, 1],
    [0, 1, 3, 1, 1, 1, 99, 1, 1]   # 0 = Final (F)
]

N = 9
energia_inicial = 18

# inicio (I) y fin (F)
inicio = (0, 8)
fin = (8, 0)

# Matriz del camino encontrado
camino = [[0]*N for _ in range(N)]

# izquierda, abajo, arriba, derecha
movs = [ (0,-1), (1,0), (-1,0), (0,1) ]

def valido(x, y):
    return 0 <= x < N and 0 <= y < N and laberinto[x][y] != 99

def backtrack(x, y, energia):

    # Si llegamos a la meta → éxito
    if (x, y) == fin:
        camino[x][y] = 1
        return True

    # Marcar celda en el camino
    camino[x][y] = 1

    # Recorrer movimientos en orden
    for dx, dy in movs:
        nx, ny = x + dx, y + dy

        if valido(nx, ny) and camino[nx][ny] == 0:

            costo = laberinto[nx][ny]

            nueva_energia = energia + costo 

            if nueva_energia >= 0:  # si aún tiene energía
                if backtrack(nx, ny, nueva_energia):
                    return True

    # Backtracking
    camino[x][y] = 0
    return False




print("LABERINTO ORIGINAL\n")
for fila in laberinto:
    print(fila)

print("\nBUSCANDO CAMINO...\n")

if backtrack(inicio[0], inicio[1], energia_inicial):
    print("¡Se encontró un camino con energía suficiente!\n")
else:
    print("NO se pudo llegar con la energía disponible.\n")

print("MATRIZ DE CAMINO (1 = usado, 0 = no usado):\n")
for fila in camino:
    print(fila)
