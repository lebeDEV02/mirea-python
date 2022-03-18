import numpy as np

i = int(input("Введите количество строк в матрице: "))
q = int(input("Введите количество столбцов в матрице: "))

matrix = np.random.randint(-10, 40, i*q)

matrix.resize((i, q))

copy = matrix.copy()
n = int(input("n: "))
k = int(input("k: "))

print("Исходная матрица: ", matrix)

copyOfNRow = copy[n]

matrix[n] = matrix[k]
matrix[k] = copyOfNRow

print("Мутированная матрица: ", matrix)
