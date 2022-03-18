import numpy as np

i = int(input("Введите количество строк в матрице: "))
q = int(input("Введите количество столбцов в матрице: "))

matrix = np.random.randint(-10, 40, i*q)

copyOfMatrix = matrix
copyOfMatrix.resize((i, q))

print("Исходная матрица A = ")
print(copyOfMatrix)

matrix = np.square(matrix)

print("Матрица A^2 = ")
matrix.resize((i, q))
print(matrix)