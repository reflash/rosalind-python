import unittest
from main import positions

# python -m unittest tests
class SearchSubTestCase(unittest.TestCase):

    def test_input(self):
        c,s_c = 'GATATATGCATATACTT','ATAT'
        self.assertEqual(positions(c,s_c), '2 4 10')

    def test_file(self):
        f = open('input.txt', 'r')
        c,s_c = f.read().strip().split()
        print(positions(c,s_c))
        f.close()
