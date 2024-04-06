#!/usr/bin/python
import sys

def decrypt(text: str, d: int, n: int) -> str:
  try:
    # Convert the encrypted string into an integer
    cyphertext_int = int(text)

    # Calculate the plaintext m (in integer form) according to the formula c^d = (m^e)^d = m, where c is the cyphertext (in integer form)
    plaintext_int = pow(cyphertext_int, d, n)

    # Convert m from integer form back to the original string
    plaintext_bytes = plaintext_int.to_bytes((n.bit_length() + 7) // 8, 'big')
    plaintext = plaintext_bytes.strip(b'\x00').decode('utf-8')
    return plaintext
  except:
    return 'Decryption Error!'

def main():
  if len(sys.argv) != 4:
    print('Usage: ./decrypt.py text d n')
    sys.exit(1)

  cyphertext = sys.argv[1]
  d = int(sys.argv[2])
  n = int(sys.argv[3])

  decrypted_text = decrypt(cyphertext, d, n)
  print(f'Decrypted Text: {decrypted_text}')

if __name__ == '__main__':
  main()