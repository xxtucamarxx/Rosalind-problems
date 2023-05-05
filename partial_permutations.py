from math import factorial


def pp(n, k):
    return (factorial(n)/factorial(n-k)) % 1000000

print(int(pp(95, 9)))
