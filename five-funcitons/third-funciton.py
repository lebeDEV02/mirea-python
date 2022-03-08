from math import sin


def main(n, b):
    firstterm = 0
    secondterm = 0
    for c in range(1, n+1, 1):
        firstterm += pow(c, 1/7)
    firstterm *= 70

    for j in range(1, b+1, 1):
        expofsecondterm = (pow(j, 3) / 46) + 1 + 93*j
        secondterm += 9 * sin(25 + j + pow(j, 3)) + pow(expofsecondterm, 4)
    return firstterm + secondterm

if __name__ == "__main__":
    main(8, 4)
