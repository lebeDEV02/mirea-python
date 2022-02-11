import math
x = float(input("X = "))
accuracy = float(input("e is "))
s=(math.pi/2)
t=0
k=1


while math.fabs(t) > accuracy:
    t += (math.factorial(2*k)*math.pow(x, 2*k+1))/(math.pow(2, 2*k) * math.pow(math.factorial(k), 2) * (2*k+1))
    k+=1
    s -= t
    print(math.radians(s))
    print(math.radians(math.acos(x)))