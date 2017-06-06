import unittest
from functional import seq
from main import probability

# python -m unittest tests
class MendelLawTestCase(unittest.TestCase):

    def test_prob(self):
        k,m,n = 2,2,2
        self.assertEqual(probability(k,m,n), 0.78333)

    def test_prob_file(self):
        f = open('rosalind_inh.txt', 'r')
        k,m,n = seq(f.read().strip().split()).map(int)
        r = probability(k,m,n)
        print(r)
        f.close()
