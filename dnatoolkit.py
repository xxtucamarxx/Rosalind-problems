from structures import *
from collections import Counter
from Bio import SeqIO


def read_fasta(arqv):
    seqs = {}
    with open(arqv) as arqv:
        for string in SeqIO.parse(arqv, "fasta"):
            seqs[string.id] = (str(string.seq))
        return seqs


def validate_dnaseq(dnaseq):
    """Checks if seq is valid DNA string"""
    tmpseq = dnaseq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides['dna']:
            return False
    return tmpseq


def dna_pair_seq(dnaseq):
    mapping = str.maketrans("ATCG", "TAGC")
    return dnaseq.translate(mapping)[::-1]


def count_nuc_freq(seq):
    """Counts the frequencie of nucleotides"""
    if "U" in seq:
        tmp_freq_dict = {
            "A": 0,
            "C": 0,
            "G": 0,
            "U": 0
        }
    else:
        tmp_freq_dict = {
            "A": 0,
            "C": 0,
            "G": 0,
            "T": 0
        }
    for nuc in tmp_freq_dict:
        tmp_freq_dict[nuc] = seq.count(nuc)
    return tmp_freq_dict


def transcript(dnaseq):
    """Replaces Ts for Us"""
    return dnaseq.replace("T", "U")


def translate(seq, format="string", init_pos=0):
    """Converts RNA string into protein"""

    def string(seq, init_pos):
        if seq.count('U'):
            return "".join([rna_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)])
        else:
            return "".join([dna_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)])

    def dicio(seq, init_pos):
        if seq.count('U'):
            return {pos + 1: rna_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)}
        else:
            return {pos + 1: dna_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)}

    execut = {"string": string(seq, init_pos),
              "dicio": dicio(seq, init_pos)}
    return execut[format]



def gc_content(seq):
    """GC content in dna/rna seq"""
    return round(((seq.count("G") + seq.count("C")) / len(seq)), 2)


def gc_content_subset(seq, k=20):
    """Counts the content of G and C in a sequence"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res


def find_motif(seq, motif):
    """Finds the location of a given motif in a strand of NA"""
    return ' '.join([str(nuc + 1) for nuc in range(len(seq) - len(motif) - 1) if seq[nuc:nuc + len(motif)] == motif])


def codon_usage(seq, aminoacid):
    """Counts amminocid frequency in sequences"""
    v = []
    total = translate(seq).count(aminoacid)
    for nuc in range(0, len(seq) - 2, 3):
        if rna_codons[seq[nuc:nuc + 3]] == aminoacid:
            v.append(seq[nuc:nuc + 3])
    freqdict = dict(Counter(v))
    print(f'{aminoacid} = {total}')
    return {i: round(j / total, 2) for i, j in freqdict.items()}


def gen_reading_frames(seq):
    res = []
    res.append(translate(seq, 0))
    res.append(translate(seq, 1))
    res.append(translate(seq, 2))
    res.append(translate(dna_pair_seq(seq), 0))
    res.append(translate(dna_pair_seq(seq), 1))
    res.append(translate(dna_pair_seq(seq), 2))
    return res


def protein_from_rf(aa_seq: list):
    """Gets all proteins from aminoacid sequence"""
    current = []
    proteins = []
    for aa in aa_seq:
        if aa == '_':
            proteins.append(current)
            current = []
        else:
            if aa == 'M':
                current.append('')
            for i in range(len(current)):
                current[i] += aa.upper()
    return proteins
