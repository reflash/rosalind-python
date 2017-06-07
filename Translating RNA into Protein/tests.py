import unittest
from main import decode

# python -m unittest tests
class RnaToProteinTestCase(unittest.TestCase):

    def test_input(self):
        rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        self.assertEqual(decode(rna), 'MAMAPRTEINSTRING')

    def test_file(self):
        f = open('input.txt', 'r')
        rna = f.read().strip()
        print(decode(rna))
        f.close()
