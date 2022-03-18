import numpy as np

i = int(input("Введите количество строк в матрице: "))
q = int(input("Введите количество столбцов в матрице: "))

matrix = np.random.randint(-10, 40, i*q)

matrix.resize((i, q))

print("Исходная матрица:")
print(matrix)

print("Элементы главной диагонали -", np.diag(matrix, 0))

topDiagonalLine = 1
bottomDiagonalLine = -1

topVerticalMatrix = []
bottomVerticalMatrix = []
while matrix.diagonal(topDiagonalLine).size != 0:
    topVerticalMatrix.append(np.array(matrix.diagonal(topDiagonalLine)))
    topDiagonalLine += 1
while matrix.diagonal(bottomDiagonalLine).size != 0:
    bottomVerticalMatrix.append(np.array(matrix.diagonal(bottomDiagonalLine)))
    bottomDiagonalLine -= 1

topVerticalMatrix = np.concatenate(topVerticalMatrix)
bottomVerticalMatrix = np.concatenate(bottomVerticalMatrix)

print("Верхняя диагональная матрица")
print(np.matrix(topVerticalMatrix))
print("Нижняя диагональная матрица")
print(np.matrix(bottomVerticalMatrix))



