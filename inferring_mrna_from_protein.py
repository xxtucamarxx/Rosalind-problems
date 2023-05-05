from structures import aminoacids_codon_freq

seq = "MA"

poss = 1

for e in seq:
      poss *= aminoacids_codon_freq[e]

print((poss*3) % 1000000)