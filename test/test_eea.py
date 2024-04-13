import sys
import unittest

sys.path.append('../')
from functions import extended_gcd

from sympy import prevprime
import random


class TestExtendedEuclideanAlgorithm(unittest.TestCase):

  def test_positive_numbers(self):
    gcd, x, y = extended_gcd(240, 46)
    self.assertEqual(gcd, 2)
    self.assertEqual(240 * x + 46 * y, gcd)

    gcd, x, y = extended_gcd(123456, 789012)
    self.assertEqual(gcd, 12)
    self.assertEqual(123456 * x + 789012 * y, gcd)

    gcd, x, y = extended_gcd(65345, 323160)
    self.assertEqual(gcd, 5)
    self.assertEqual(65345 * x + 323160 * y, gcd)

    gcd, x, y = extended_gcd(2330646462, 3044333)
    self.assertEqual(gcd, 1)
    self.assertEqual(2330646462 * x + 3044333 * y, gcd)

    gcd, x, y = extended_gcd(926467262, 6430314335)
    self.assertEqual(gcd, 1)
    self.assertEqual(926467262 * x + 6430314335 * y, gcd)

  def test_one_zero(self):
    gcd, x, y = extended_gcd(7, 0)
    self.assertEqual(gcd, 7)
    self.assertEqual(7 * x + 0 * y, gcd)

    gcd, x, y = extended_gcd(0, 239402839)
    self.assertEqual(gcd, 239402839)
    self.assertEqual(0 * x + 239402839 * y, gcd)

    gcd, x, y = extended_gcd(0, 29342093849283409283984234)
    self.assertEqual(gcd, 29342093849283409283984234)
    self.assertEqual(0 * x + 29342093849283409283984234 * y, gcd)

    gcd, x, y = extended_gcd(888888888888888888888888, 0)
    self.assertEqual(gcd, 888888888888888888888888)
    self.assertEqual(888888888888888888888888 * x + 0 * y, gcd)

    gcd, x, y = extended_gcd(10**100, 0)
    self.assertEqual(gcd, 10**100)
    self.assertEqual(10**100 * x + 0 * y, gcd)

  def test_both_zeros(self):
    gcd, x, y = extended_gcd(0, 0)
    self.assertEqual(gcd, 0)
    self.assertEqual(0 * x + 0 * y, gcd)

  def test_negative_numbers(self):
    gcd, x, y = extended_gcd(-120, 23)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs((-120) * x + 23 * y), gcd)

    gcd, x, y = extended_gcd(-120, 23)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs((-120) * x + 23 * y), gcd)

    gcd, x, y = extended_gcd(-15, 4)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs((-15) * x + 4 * y), gcd)

    gcd, x, y = extended_gcd(-123456, 78901)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs((-123456) * x + 78901 * y), gcd)

    gcd, x, y = extended_gcd(101, -50)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs(101 * x + (-50) * y), gcd)

    gcd, x, y = extended_gcd(100000, -45000)
    self.assertEqual(gcd, 5000)
    self.assertEqual(abs(100000 * x + (-45000) * y), gcd)

  def test_both_negatives(self):
    gcd, x, y = extended_gcd(-10, -25)
    self.assertEqual(gcd, 5)
    self.assertEqual(abs((-10) * x + (-25) * y), gcd)

    gcd, x, y = extended_gcd(-120, -360)
    self.assertEqual(gcd, 120)
    self.assertEqual(abs((-120) * x + (-360) * y), gcd)

    gcd, x, y = extended_gcd(-123456, -789012)
    self.assertEqual(gcd, 12)
    self.assertEqual(abs((-123456) * x + (-789012) * y), gcd)

    gcd, x, y = extended_gcd(-101, -103)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs((-101) * x + (-103) * y), gcd)

    gcd, x, y = extended_gcd(-1001, -997)
    self.assertEqual(gcd, 1)
    self.assertEqual(abs((-1001) * x + (-997) * y), gcd)

  def test_very_large_numbers(self):
    large_prime_1 = prevprime(10**50)
    large_prime_2 = prevprime(10**100)
    gcd, x, y = extended_gcd(large_prime_1, large_prime_2)
    self.assertEqual(gcd, 1)
    self.assertEqual(large_prime_1 * x + large_prime_2 * y, gcd)

    random_num = random.randint(1, 10**50)
    gcd, x, y = extended_gcd(random_num, random_num * large_prime_2)
    self.assertEqual(gcd, random_num)
    self.assertEqual(random_num * x + random_num * large_prime_2 * y, gcd)

    random_num = random.randint(1, 10**50)
    large_prime_2 = prevprime(10**500)
    gcd, x, y = extended_gcd(random_num, random_num * large_prime_2)
    self.assertEqual(gcd, random_num)
    self.assertEqual(random_num * x + random_num * large_prime_2 * y, gcd)

    random_num = random.randint(1, 10**50)
    large_prime_2 = prevprime(10**750)
    gcd, x, y = extended_gcd(random_num, random_num * large_prime_2)
    self.assertEqual(gcd, random_num)
    self.assertEqual(random_num * x + random_num * large_prime_2 * y, gcd)

    random_num = random.randint(1, 10**50)
    large_prime_2 = prevprime(10**1000)
    gcd, x, y = extended_gcd(random_num, random_num * large_prime_2)
    self.assertEqual(gcd, random_num)
    self.assertEqual(random_num * x + random_num * large_prime_2 * y, gcd)


if __name__ == '__main__':
  unittest.main()
