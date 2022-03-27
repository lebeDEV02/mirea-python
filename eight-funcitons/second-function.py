import math


def main(y):
    if y < 8:
        return 1 + 97 * pow(y, 4)
    elif 8 <= y < 94:
        return pow(y, 7)
    elif 94 <= y < 125:
        return pow(math.log(y), 6)
    else:
        return pow(y, 3) + 44 * (pow(y, 4) + pow(y, 5))


if __name__ == "__main__":
    print(main(26))
