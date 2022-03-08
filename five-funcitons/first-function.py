def main(x):
    firstTerm = pow((1 - 42 * x - (pow(x, 2) / 44)), 3) / 84
    partOfSecondTerm = pow(x, 3) - 48 * x - 27 * pow(x, 2)
    secondTerm = (pow(x, 4)) / (1 + pow(partOfSecondTerm, 4))
    return firstTerm - secondTerm



if __name__ == "__main__":
    main()
