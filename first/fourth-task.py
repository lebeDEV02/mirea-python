n = int(input("Enter size of matrix: "))

matrix = []
print("Enter the entries row sise:")

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

def printMatrix(size, matrix, matrixType):
    print(matrixType + ": ")
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print()

def rearrangeMatrix(size, matrix):
    for k in range (size):
        max = matrix[0][0]
        max_i = 0
        max_j = 1
        for i in range (size):
            for j in range(size):
                if not(i == j and i < k):
                    if matrix[i][j] > matrix[max_i][max_j]:
                        max_i = i
                        max_j = j
        max = matrix[max_i][max_j]
        matrix[max_i][max_j] = matrix[k][k]
        matrix[k][k] = max
    printMatrix(n, matrix, "Матрица с перестановками")

def findRowWithoutPositive(size, matrix):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] <= 0:
                if(j == size - 1):
                    print('Первая строка без положительных элементов - ' + str(i+1) + ' строка')
                    return
                else:
                    continue
            elif i < size-1:
                continue
            elif i == size - 1:
                print('Нет строк без положительных элементов')
                return

printMatrix(n, matrix, 'Исходная матрица')

rearrangeMatrix(n, matrix)

findRowWithoutPositive(n, matrix)