#!/usr/bin/python
import sys


def encrypt(text: str, n: int, e: int) -> str:
  # Convert the given string into an integer using utf-8 encoding
  plaintext_int = int.from_bytes(text.encode('utf-8'), 'big')

  # Compute the cyphertext c (in integer form) according to the formula c = m^e mod n
  cyphertext_int = pow(plaintext_int, e, n)

  return str(cyphertext_int)


def main():
  if len(sys.argv) != 4:
    print('Usage: ./encrypt.py text n e')
    sys.exit(1)

  text = sys.argv[1]
  n = int(sys.argv[2])
  e = int(sys.argv[3])

  encrypted_text = encrypt(text, n, e)
  print(f'Encrypted Text: {encrypted_text}')


if __name__ == '__main__':
  main()
