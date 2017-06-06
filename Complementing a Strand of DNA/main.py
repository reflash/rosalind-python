from functional import seq

def nucleus_pair(x):
    if x == 'A':
        return 'T'
    elif x == 'T':
        return 'A'
    elif x == 'C':
        return 'G'
    elif x == 'G':
        return 'C'
    else:
        raise ValueError("This nucleotid component could not appear in DNA", x)

def test1():
    strand = 'GTCA'
    dna_nts = seq(list(reversed(strand)))
    result = ''.join(dna_nts.map(lambda x: nucleus_pair(x)))
    assert result == 'TGAC'
    print("Success " + result)

def test2():
    strand = 'AAAACCCGGT'
    dna_nts = seq(list(reversed(strand)))
    result = ''.join(dna_nts.map(lambda x: nucleus_pair(x)))
    assert result == 'ACCGGGTTTT'
    print("Success " + result)

f = open('rosalind_revc.txt', 'r')
dna_nts = seq(list(reversed(f.read().strip())))
paired_nts = dna_nts.map(lambda x: nucleus_pair(x))
print(''.join(paired_nts))
