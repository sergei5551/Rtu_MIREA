from math import log10


def main(m, n, b, p):
    f = 0
    for k in range(1, b+1):
        for c in range(1, n+1):
            for i in range(1, m+1):
                f += log10((p**2)/68+77+5*k) + pow(log10(86*i-10-(c**2)), 2)
    return f


'''
print(main(4, 6, 7, -0.11))  # ≈ 1.16e+03
print(main(4, 7, 7, -0.54))  # ≈ 1.34e+03
print(main(6, 8, 2, 0.18))  # ≈ 7.12e+02
print(main(2, 7, 3, 0.79))  # ≈ 2.41e+02
print(main(5, 5, 5, -0.23))  # ≈ 9.15e+02
'''


def main(m, n, b, p):
    # Используем генератор списка для вычисления суммы
    return sum(
        log10((p**2) / 68 + 77 + 5 * k) + pow(log10(86 * i - 10 - (c**2)), 2)
        for k in range(1, b + 1)
        for c in range(1, n + 1)
        for i in range(1, m + 1)
    )
