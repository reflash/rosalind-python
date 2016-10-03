from itertools import groupby
from operator import itemgetter

def accumulate(l):
    it = groupby(l, itemgetter(0))
    for key, subiter in it:
       yield key, sum(item[1] for item in subiter)

f = open('rosalind_dna.txt', 'r')
dna = f.read().strip()
for nucl,count in list(
                accumulate(
                sorted(
                map(lambda x: (x,1), dna)))):
    print(count, end=' ')
