import math
n = float(input("n = "))
m = float(input("m = "))

z1 = ((m-1)*math.sqrt(m)-(n-1)*math.sqrt(n))/(math.sqrt(pow(m,3)*n)+n*m+pow(m,2)-m)
z2 = ((math.sqrt(m) - math.sqrt(n))/m)


print(z1, z2)