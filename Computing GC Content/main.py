from functional import seq

f = open('rosalind_fasta.txt', 'r')
x = f.read().strip().split('>')
x.pop(0)

x = ( seq(x)
        .map(lambda s: s.split())
        .map(lambda s: (s.pop(0), ''.join(s)))
        .map(lambda n_d: (n_d[0], (n_d[1].count('C') + n_d[1].count('G')) / len(n_d[1]) * 100))
    )
    
max = max(x, key=lambda a: a[1])
print(max[0])
print(max[1])
