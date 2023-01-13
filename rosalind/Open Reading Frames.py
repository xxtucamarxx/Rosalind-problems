from DNAtoolkit import gen_reading_frames
from Bio import SeqIO
import re

seq = str(SeqIO.read("file.txt", "fasta").seq)
pattern = re.compile("M[A-Z]*_")

prots = gen_reading_frames(seq)
openreads = []

for prot in prots:
    efetivo = pattern.findall(prot)
    openreads.extend(efetivo)

for e in set(openreads):
    print(e[:-1])
    e = e[1:]
    prox = len(re.findall("M", e))
    for i in range(prox):
        print(pattern.search(e).group()[:-1])
        e = e[e.find("M")+1:]
