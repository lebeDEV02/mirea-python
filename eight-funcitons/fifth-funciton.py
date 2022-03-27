import math
from math import cos


def main(listelem):
    result = 0
    for i in range(1, len(listelem)+1, 1):
        result += 31*cos(1+45*pow(listelem[len(listelem)-math.ceil(i/3)], 2))
    return result


if __name__ == "__main__":
    print(main([-0.12, -0.63, 0.95, -0.23, -0.05, 0.9, 0.71, 0.05]))
