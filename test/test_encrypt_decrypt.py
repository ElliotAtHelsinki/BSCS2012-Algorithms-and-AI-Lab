import sys
import unittest

sys.path.append('../../')
from generate import generate
from encrypt import encrypt
from decrypt import decrypt


class TestEncryptDecrypt(unittest.TestCase):
  def test_encrypt_decrypt(self):
    ORIGINAL_STRING = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    (n, e, d) = generate()
    encrypted = encrypt(ORIGINAL_STRING, n, e)
    self.assertNotEqual(ORIGINAL_STRING, encrypted, 'The encrypted string is not the same as the original string.')
    self.assertIsInstance(encrypted, str, 'The result of the encryption is indeed a string.')
    decrypted = decrypt(encrypted, d, n)
    self.assertEqual(ORIGINAL_STRING, decrypted, 'The decrypted string matches the original string.')


if __name__ == '__main__':
  unittest.main()
