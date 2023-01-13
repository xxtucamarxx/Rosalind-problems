from itertools import permutations


def fac(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fac(x-1)


p = 6
print(fac(p))
for e in list(permutations(range(1, p+1))):
    print(' '.join(map(str, list(e))))
