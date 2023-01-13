from DNAtoolkit import dna_pair_seq
from Bio import SeqIO


seq = str(SeqIO.read("file.txt", "fasta").seq)

write = []
for e, _ in enumerate(seq):
    for i, nuc in enumerate(seq, 1):
        atual = seq[e:i]
        tamanho = len(atual)
        if 4 <= tamanho <= 12 and atual == dna_pair_seq(atual):
            escr = f"{e+1} {tamanho}"
            write.append(escr)

with open("resultado.txt", "w") as file:
    for e in write:
        file.write(e)
        file.write("\n")
