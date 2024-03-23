import sys
import unittest

sys.path.append('../')
from functions import primality_test


class TestPrimalityChecker(unittest.TestCase):

  def test_prime_number(self):
    self.assertTrue(primality_test(5), msg="5 is a prime number.")
    self.assertTrue(primality_test(7), msg="7 is a prime number.")
    self.assertTrue(primality_test(29), msg="29 is a prime number.")
    self.assertTrue(primality_test(34841), msg="34841 is a prime number.")
    self.assertTrue(primality_test(8328989), msg="34841 is a prime number.")
    # self.assertTrue(primality_test(2**82589933-1), msg="The largest known prime number is a prime number.")

  def test_non_prime_number(self):
    self.assertFalse(primality_test(4), msg="4 is not a prime number.")
    self.assertFalse(primality_test(6), msg="6 is not a prime number.")
    self.assertFalse(primality_test(8), msg="8 is not a prime number.")
    self.assertFalse(primality_test(17650839),
                     msg="17,650,839 is not a prime number.")

  def test_edge_cases(self):
    self.assertFalse(primality_test(0), msg="0 is not a prime number.")
    self.assertFalse(primality_test(1), msg="1 is not a prime number.")
    self.assertTrue(primality_test(2), msg="2 is a prime number.")
    self.assertTrue(primality_test(3), msg="3 is a prime number.")


if __name__ == '__main__':
  unittest.main()
