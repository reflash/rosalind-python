from functional import seq

def dna_to_rna(x):
    if x == 'A' or x == 'C' or x == 'G':
        return x
    elif x == 'T':
        return 'U'
    else:
        raise ValueError("This nucleotid component could not appear in DNA", x)

f = open('rosalind_rna.txt', 'r')
dna_nts = seq(list(f.read().strip()))
rna_nts = dna_nts.map(lambda x: dna_to_rna(x))
print(''.join(rna_nts))
