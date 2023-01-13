from Bio import SeqIO

k = 3
arqv = 'rosalind_grph.txt'
grupo = {}

with open(arqv) as arqv:
    for string in SeqIO.parse(arqv, "fasta"):
        grupo[string.id] = [str(string.seq[:k]), str(string.seq[-k:])]

for e, i in grupo.items():
    for j, k in grupo.items():
        if k != i and i[1] == k[0]:
            print(e, j)
