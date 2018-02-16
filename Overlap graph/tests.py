import unittest
from main import overlap_graph

k = 3
# python -m unittest tests
class OverlapGraphTestCase(unittest.TestCase):

    def test_input(self):
        data = '''>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG'''

        self.assertEqual(overlap_graph(k, data),
'''Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323''')

    def test_file(self):
        f = open('input.txt', 'r')
        data = f.read().strip()
        print(overlap_graph(k, data))
        f.close()
