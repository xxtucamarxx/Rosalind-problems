from structures import aminoacids_weight

arqv = "rosalind_prtm.txt"

with open(arqv) as arqv:
    prot = list(arqv.read().strip("\n"))


weight = 0
for amino in prot:
    weight += aminoacids_weight[amino]

print(round(weight, 3))