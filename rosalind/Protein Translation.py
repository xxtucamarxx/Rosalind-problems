from DNAtoolkit import translate
import re

file = "file.txt"

with open(file) as f:
    seq = f.readline()
    amino = f.readline()

prot = translate(seq, "dicio")

for key, value in prot.items():
    if value == "M":
        print(key)
        break
