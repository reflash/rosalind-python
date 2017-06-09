import unittest
from main import profile_consensus

# python -m unittest tests
class SearchSubTestCase(unittest.TestCase):

    def test_input(self):
        data = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''

        self.assertEqual(profile_consensus(data),
'''ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6''')

    def test_file(self):
        f = open('input.txt', 'r')
        data = f.read().strip()
        print(profile_consensus(data))
        f.close()
