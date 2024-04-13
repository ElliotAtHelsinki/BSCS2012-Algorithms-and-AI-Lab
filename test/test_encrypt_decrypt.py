import sys
import unittest

sys.path.append('../../')
from generate import generate
from encrypt import encrypt
from decrypt import decrypt


class TestEncryptDecrypt(unittest.TestCase):

  def test_encrypt_decrypt(self):
    test_strings = [
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
      '没有共产党就没有新中国',
      'nolla yksi kaksi kolme neljä viisi kuusi seitsemän kahdeksan yhdeksän kymmenen',
      'Jag förstår inte.',
      '12 апреля 1961 года Юрий Гагарин стал первым человеком в мировой истории, совершившим полёт в космическое пространство.'
    ]
    for ORIGINAL_STRING in test_strings:
      (n, e, d) = generate()
      encrypted = encrypt(ORIGINAL_STRING, n, e)
      self.assertNotEqual(ORIGINAL_STRING, encrypted, 'The encrypted string is not the same as the original string.')
      self.assertIsInstance(encrypted, str, 'The result of the encryption is indeed a string.')
      decrypted = decrypt(encrypted, d, n)
      self.assertEqual(ORIGINAL_STRING, decrypted, 'The decrypted string matches the original string.')


if __name__ == '__main__':
  unittest.main()
