from DNAtoolkit import translate
import re
from Bio import SeqIO

seqs = list(SeqIO.parse("file.txt", "fasta"))

seq = str(seqs[0].seq)
introns = [str(intron.seq) for intron in seqs[1:]]
introns = sorted(introns, key=len)

for intron in introns:
    seq = seq.replace(intron, "")

print(translate(seq)[:-1])

