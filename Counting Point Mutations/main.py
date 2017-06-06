from functional import seq

f = open('rosalind_dna2.txt', 'r')
d1,d2 = f.read().strip().split()

count = ( seq(zip(d1,d2))
        .map(lambda d1_d2: d1_d2[0] != d1_d2[1])
        .sum()
)

print(count)
