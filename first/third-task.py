import math

n = int(input("Элементов в массиве N: "))
if n > 0:
    generalArray = []
    arrayWithBaseLowerThen1 = []
    arrayWithBaseHigherThen1 = []
    amountOfPositiveNumbers = 0
    indexOfZero = -1
    for i in range (0, n):
        readInput = float(input("Введите " + str(i+1) +  " элемент массива - "))
        generalArray.append(readInput)
        if readInput > 0:
            amountOfPositiveNumbers += 1
        elif readInput==0:
            indexOfZero = i
        if math.floor(readInput) <= 1:
            arrayWithBaseLowerThen1.append(readInput)
        else:
            arrayWithBaseHigherThen1.append(readInput)


    if indexOfZero >=0:
        sumOfElements = 0
        for i in range (len(generalArray) - indexOfZero):
            sumOfElements += generalArray[i]


    print('Число положительных чисел = ' + str(amountOfPositiveNumbers))
    if indexOfZero >=0:
        print('Сумма элементвов после последнего нуля = ' + str(sumOfElements))
    else:
        print('Нет нуля в массиве!')

    arrayWithBaseLowerThen1 = sorted(arrayWithBaseLowerThen1)
    arrayWithBaseHigherThen1 = sorted(arrayWithBaseHigherThen1)
    print('Массив с отсортированными значениями - ' + str([*arrayWithBaseLowerThen1, *arrayWithBaseHigherThen1]))
else:
    print('Число чисел должно быть больше 0!')

# print('Массив с отсортированными значениями - ' + str([*arrayWithBaseLowerThen1, *arrayWithBaseHigherThen1]))