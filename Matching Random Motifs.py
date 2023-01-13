from numpy import prod

file = "file.txt"

with open(file) as file:
    N, x, seq = file.read().split()

N = int(N)
x = float(x)
tam = len(seq)
prob = dict(C=x / 2, G=x / 2, A=(1 - x) / 2, T=(1 - x) / 2)

prob = 1 - (prod([prob[i] for i in seq]))

print(round(1 - (prob ** N), 3))
