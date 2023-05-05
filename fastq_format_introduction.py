from Bio import SeqIO

record = SeqIO.parse("file.txt", "fastq")

with open("resultado.txt", "w") as file:
    SeqIO.write(record, file, "fasta")

