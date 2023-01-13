from Bio import Entrez

termo = 'Platalea'
date1 = '2011/04/02'
date2 = '2011/11/10'

Entrez.email = "arthur.a.delacerda@hotmail.com"

with Entrez.esearch(db='nucleotide', term=f"{termo}[Organism]", mindate=date1, maxdate=date2, datetype='pdat') as handle:
    record = Entrez.read(handle)
    print(record["Count"])
