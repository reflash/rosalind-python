import unittest
from main import total

# python -m unittest tests
class MortalFibTestCase(unittest.TestCase):

    def test_input(self):
        n,m = 6,3
        self.assertEqual(total(n,m), 4)

    def test_file(self):
        f = open('input.txt', 'r')
        n,m = map(int, f.read().strip().split())
        print(total(n,m))
        f.close()
