# 1
def main(n):
    if n == 0:
        return -0.05
    elif n >= 1:
        return pow(main(n-1), 2) - 1 - main(n-1)


# 2
lambda n: -0.05 if n == 0 else pow(main(n-1), 2) - 1 - main(n-1)

