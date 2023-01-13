from Bio import Entrez
from Bio import SeqIO

with open('file.txt')as file:
    genes = file.read().split()

Entrez.email = "arthur.a.delacerda@hotmail.com"

with Entrez.efetch(db='nucleotide', id=genes, rettype="fasta") as handle:
    records = list(SeqIO.parse(handle, "fasta"))

seqs = [e.seq for e in records]
index = seqs.index(min(seqs, key=len))

with open("resultado.txt", "w") as file:
    SeqIO.write(records[index], file, "fasta")

