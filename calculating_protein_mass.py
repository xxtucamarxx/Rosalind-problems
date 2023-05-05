from structures import aminoacids_weight

def solve(arqv):
    with open(arqv) as arqv:
        prot = list(arqv.read().strip("\n"))

    weight = 0
    for amino in prot:
        weight += aminoacids_weight[amino]

    print(round(weight, 3))
    
solve("rosalind_prtm.txt")
