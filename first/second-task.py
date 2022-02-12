import math

x = float(input("X = "))
accuracy = float(input("e is "))
s = currentTerm = float((math.pi/2))
t = float(0)
k = int(0)

while math.fabs(currentTerm) > accuracy:
    item = (math.factorial(2*k)*math.pow(x, 2*k+1))/(math.pow(2, 2*k) * math.pow(math.factorial(k), 2) * (2*k+1))
    s -= item
    k += 1
    print("Приближенное значение = ", s)
    print("Точное значение = ", math.acos(x))
