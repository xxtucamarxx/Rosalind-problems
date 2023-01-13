from itertools import product

with open("file.txt") as file:
    alph, n = file.readlines()


alph = alph.split()
n = int(n)
alph.insert(0, "")

print(alph)
combs = []

for i in range(n+1):
    for e in list(product(alph, repeat=i)):
        combs.append(''.join(map(str, list(e))))

for i in sorted(combs):
    print(i)