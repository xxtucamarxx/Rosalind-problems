from Bio import SeqIO
import numpy as np

file = "file.txt"

with open(file, "r") as f:
    q, p = f.readline().split()
    lines = f.readlines()
with open(file, "w") as f:
    for line in lines:
        f.write(line)


seqs = SeqIO.parse(file, "fastq")


print(q)
print(p)