import sys
import unittest
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

    large_prime = (2**32 + 1) // 641
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = (10**18 + 1) // 1000001
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = 170141183460469231731687303715884105727
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = 180 * large_prime**2 + 1
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

    large_prime = 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
    self.assertTrue(primality_test(large_prime), msg=f'{large_prime} is a prime number.')

  def test_non_prime_number(self):
    self.assertFalse(primality_test(4), msg='4 is not a prime number.')
    self.assertFalse(primality_test(6), msg='6 is not a prime number.')
    self.assertFalse(primality_test(8), msg='8 is not a prime number.')
    self.assertFalse(primality_test(17650839), msg='17650839 is not a prime number.')

    large_non_prime = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151 + 1
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_prime = (2**64 + 1) // 274177
    large_prime_2 = (2 * 32 + 1) // 641
    large_non_prime = large_prime * large_prime_2
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_non_prime = large_prime * random.randint(1, 10**1000)
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_non_prime = large_prime_2 * random.randint(1, 7**750)
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_non_prime = random.randint(1, 10**1000) * random.randint(1, 10**1000)
    self.assertFalse(primality_test(large_non_prime), msg=f'{large_non_prime} is not a prime number.')

    large_prime = 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
    large_prime_2 = (2**64 + 1) // 274177
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
