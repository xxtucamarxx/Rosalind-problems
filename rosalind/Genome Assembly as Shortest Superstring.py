from Bio import SeqIO
from itertools import permutations
import re


def prefixes(seq):
    """
   Return a list of all the prefixes of the given seq (including itself), in ascending order (from shortest to longest).
   """
    return (seq[:i] for i, _ in enumerate(seq, 1) if len(seq[:i]) > len(seq) / 2)


def overlap(seqs: list):
    contig = ''
    for seq in seqs:
        if seq in contig:
            continue
        for prefix in prefixes(seq):
            if contig.endswith(prefix):
                fim = re.search(prefix, seq).end()
                contig += seq[fim:]
                break
        else:
            contig += seq
    return contig


def solve(seqs):
    return min((overlap(list(seq_perms)) for seq_perms in permutations(seqs)), key=len)


seqs = (str(seq.seq) for seq in list(SeqIO.parse("file.txt", "fasta")))

print(solve(seqs))

