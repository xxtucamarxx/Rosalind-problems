from math import log10

file = "rosalind_prob.txt"

with open(file) as file:
    seq, probs = file.read().splitlines()

probs = [float(x) for x in probs.split(' ')]

match = {x: dict(
    C=y / 2,
    G=y / 2,
    A=(1 - y) / 2,
    T=(1 - y) / 2) for x, y in enumerate(probs)}

probabilities = [1.0 for _, _ in enumerate(probs)]

for i, _ in enumerate(probabilities):
    probability = 1
    for nuc in seq:
        probability *= match[i][nuc]
    probabilities[i] = round(log10(probability), 3)

print(' '.join(map(str, probabilities)))

