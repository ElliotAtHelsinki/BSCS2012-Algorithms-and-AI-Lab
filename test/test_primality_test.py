import sys
import unittest
from sympy import prevprime
import random

sys.path.append('../')
from functions import primality_test


class TestPrimalityTest(unittest.TestCase):

  def test_prime_number(self):
    self.assertTrue(primality_test(5), msg='5 is a prime number.')
    self.assertTrue(primality_test(7), msg='7 is a prime number.')
    self.assertTrue(primality_test(29), msg='29 is a prime number.')
    self.assertTrue(primality_test(34841), msg='34841 is a prime number.')
    self.assertTrue(primality_test(8328989), msg='8328989 is a prime number.')

    large_prime = prevprime(10**100)
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = prevprime(10**250)
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = prevprime(10**500)
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = prevprime(10**750)
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = prevprime(10**1000)
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

  def test_non_prime_number(self):
    self.assertFalse(primality_test(4), msg='4 is not a prime number.')
    self.assertFalse(primality_test(6), msg='6 is not a prime number.')
    self.assertFalse(primality_test(8), msg='8 is not a prime number.')
    self.assertFalse(primality_test(17650839), msg='17650839 is not a prime number.')

    large_non_prime = prevprime(10**600) + 1
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_prime = prevprime(10**750)
    large_prime_2 = prevprime(10**64)
    large_non_prime = large_prime * large_prime_2

    large_non_prime = large_prime * random.randint(1, 10**1000)
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_non_prime = large_prime_2 * random.randint(1, 7**750)
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_non_prime = random.randint(1, 10**1000) * random.randint(1, 10**1000)
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_prime = prevprime(10**100)
    large_prime_2 = prevprime(10**600)
    large_non_prime = large_prime * large_prime_2
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

  def test_edge_cases(self):
    self.assertFalse(primality_test(0), msg='0 is not a prime number.')
    self.assertFalse(primality_test(1), msg='1 is not a prime number.')
    self.assertTrue(primality_test(2), msg='2 is a prime number.')
    self.assertTrue(primality_test(3), msg='3 is a prime number.')
    self.assertTrue(primality_test(5), msg='5 is a prime number.')


if __name__ == '__main__':
  unittest.main()
