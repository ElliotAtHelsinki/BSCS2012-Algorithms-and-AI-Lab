import sys
import unittest

sys.path.append('../')
from functions import extended_gcd


class TestExtendedEuclideanAlgorithm(unittest.TestCase):

  def test_positive_numbers(self):
    gcd, x, y = extended_gcd(240, 46)
    self.assertEqual(gcd, 2)
    self.assertEqual(240 * x + 46 * y, gcd)

    gcd, x, y = extended_gcd(123456, 789012)
    self.assertEqual(gcd, 12)
    self.assertEqual(123456 * x + 789012 * y, gcd)

  def test_one_zero(self):
    gcd, x, y = extended_gcd(7, 0)
    self.assertEqual(gcd, 7)
    self.assertEqual(7 * x + 0 * y, gcd)

    gcd, x, y = extended_gcd(0, 239402839)
    self.assertEqual(gcd, 239402839)
    self.assertEqual(0 * x + 239402839 * y, gcd)

  def test_both_zeros(self):
    gcd, x, y = extended_gcd(0, 0)
    self.assertEqual(gcd, 0)
    self.assertEqual(0 * x + 0 * y, gcd)

  def test_negative_numbers(self):
    gcd, x, y = extended_gcd(-120, 23)
    self.assertEqual(gcd, 1)
    self.assertEqual((-120) * x + 23 * y, gcd)


if __name__ == '__main__':
  unittest.main()
