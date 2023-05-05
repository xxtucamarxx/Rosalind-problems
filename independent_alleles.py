def fat(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fat(x-1)


def comb(x, y):
    return int(fat(x) / (fat(y) * fat(x-y)))


def prob_binomial(k, n):
    prob = 1/4
    return comb(k, n) * (prob ** n) * ((1 - prob) ** (k - n))


k = 2 ** 5
N = 9

print(sum([prob_binomial(k, n) for n in range(N, k+1)]))

