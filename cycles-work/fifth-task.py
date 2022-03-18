import numpy as np

n = int(input("Введите размер матрицы: "))

listOfEntries = []


def getarrayelement(first, second):
    return 1/(first+second-1)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        listOfEntries.append(getarrayelement(i, j))

listOfEntries = np.array(listOfEntries).reshape(n,n)

print(listOfEntries)