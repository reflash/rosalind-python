# biopython
from Bio.Seq import Seq

s = """CCCTGACTTTCAACTCTGTCTCCTTCCTCTTCCTACAGTACTCCCCTGCCCTCAACAAGATGTTTTGCCA
ACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCACGCC
ATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCT
CAGATAGCGATGGTGAGCAGCTGGGGCTGGAGAGACGACAGGGCTGGTTGCCCAGGGTCCCCAGGCCTCT
GATTCCTCACTGATTGCTCTTAGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGT
GTGGAGTATTTGGATGACAGAAACACTTTTCGACATAGTGTGGTGGTGCCCTATGAGCCGCCTGAGGTCT
GGTTTGCAACTGGGGT""".replace("\n","").replace(" ","")

F = Seq(s)[0:20]
R = Seq(s).reverse_complement()[0:20]

print(F, R)