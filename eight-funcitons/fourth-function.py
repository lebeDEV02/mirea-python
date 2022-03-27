

def main(n):
    if n == 0:
        return -0.83
    else:
        return 1 + (pow(0.01-pow(main(n-1),2)-pow(main(n-1), 3), 3)/55)


if __name__ == "__main__":
    print(main(4))
