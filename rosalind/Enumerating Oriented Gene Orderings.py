import numpy as np
from itertools import permutations
from itertools import product

n = 6

alph = [i for i in range(1, n+1)]
temp = [np.array(list(e)) for e in permutations(alph, n)]
mask = [np.array(e) for e in list(product([1, -1], repeat=n))]
combs = []

for e in temp:
    for i in mask:
        combs.append(e*i)

print(len(combs))
for e in combs:
    print(" ".join(map(str, e)))
