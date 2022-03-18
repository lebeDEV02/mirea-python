import numpy as np

firstMatrix = np.matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
secondMatrix = np.matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])

resultMatrix = np.dot(firstMatrix, secondMatrix)

print(resultMatrix)