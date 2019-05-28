from Bio.Seq import Seq

s = Seq("""ACTATCATGCTAGCATGCTTTCG""")

A_T = s.count('A') + s.count('T')
G_C = s.count('G') + s.count('C')

Tm = 4*G_C + 2*A_T

print(Tm)