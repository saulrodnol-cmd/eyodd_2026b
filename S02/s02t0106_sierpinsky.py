
from array import array as arr

# Parametros de la cuadricula
rows = 8
columns = 2 * rows - 1

# Funcion para imprimir matriz
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Creando la reticula 2D
matrix = []

# Construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la construccion del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

# Calculando el centro de la primera fila
center = columns // 2  # Se hace division entera

# Estableciendo el centro en 1
matrix[0][center] = 1

# Se calcula el resto de la matriz
# Siguiendo la logica del Sierpinsky Gasket
for row in range(1, rows):
    for column in range(0, columns):

        left_upper_cell = 0
        right_upper_cell = 0

        # Si la columna donde estamos es mayor a cero
        if column > 0:
            left_upper_cell = matrix[row - 1][column - 1]

        # Si la columna esta un elemento antes del borde derecho
        if column < columns - 1:
            right_upper_cell = matrix[row - 1][column + 1]

        # Guardar el arreglo
        if left_upper_cell != right_upper_cell:
            matrix[row][column] = 1
        else:
            matrix[row][column] = 0

# Imprimir matriz
print()
print_matrix(matrix)

# Funcion para dibujar la matriz
def draw_matrix(input_matrix, symbol="*"):
    for row in input_matrix:
        for value in row:
            if value == 1:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

# Dibujar triangulo de Sierpinski
print()
draw_matrix(matrix)
     
     