from Bio import SeqIO
from structures import aminoacids_weight
arqv = 'rosalind_prtm2.txt'

with open(arqv) as arqv:
    prot = arqv.read()

print(prot)


