from math import factorial as fac


def comb(x, y):
    return fac(x) / (fac(y) * fac(x - y))


def binomial(x, y, prob):
    return comb(x, y) * (prob ** y) * ((1 - prob) ** (x - y))


file = "file.txt"
with open(file) as file:
    n, seq, A = file.read().splitlines()


n = int(n)
A = list(map(float, A.split()))
match = {x: dict(
    C=y / 2,
    G=y / 2,
    A=(1 - y) / 2,
    T=(1 - y) / 2) for x, y in enumerate(A)}

probabilities = [1.0 for _, _ in enumerate(A)]

for i, prob in enumerate(probabilities):
    for _, nuc in enumerate(seq):
        probabilities[i] *= match[i][nuc]


print(binomial(n, 1, probabilities[0]))
