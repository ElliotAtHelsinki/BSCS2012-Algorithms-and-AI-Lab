import sys
import unittest

sys.path.append('../../')
from generate import generate


class TestGenerator(unittest.TestCase):
  def test_generate(self):
    (n, e, d) = generate()
    self.assertIsInstance(n, int, 'n is correctly returned as an integer.')
    self.assertIsInstance(e, int, 'e is correctly returned as an integer.')
    self.assertIsInstance(d, int, 'd is correctly returned as an integer.')


if __name__ == '__main__':
  unittest.main()
