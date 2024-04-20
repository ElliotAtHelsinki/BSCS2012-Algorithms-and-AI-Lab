#!/usr/bin/python
from generate import generate
from encrypt import encrypt
from decrypt import decrypt


def main():
  while True:
    choice = input("""What do you want to do?
1. Generate a new key pair
2. Encrypt a string
3. Decrypt a string
4. Exit the program

Enter your choice (1, 2, 3, or 4): """)
    if choice == '1':
      print()
      (n, e, d) = generate()
      print('A new key pair has been successfully generated!')
      print('Public key components:')
      print(f'n: {n}')
      print(f'e: {e}')
      print('Private key component:')
      print(f'd: {d}')
      print()
      pass
    elif choice == '2':
      print()
      text = input('Enter the string to encrypt: ')
      n = int(input('Enter n: '))
      e = int(input('Enter e: '))
      try:
        encrypted_text = encrypt(text, n, e)
        print(f'The string has been encrypted to: {encrypted_text}')
      except:
        print('Encryption Error!')
      print()
      pass
    elif choice == '3':
      print()
      text = input('Enter the string to decrypt: ')
      d = int(input('Enter d: '))
      n = int(input('Enter n: '))
      try:
        decrypted_text = decrypt(text, d, n)
        print(f'The string has been decrypted to: {decrypted_text}')
      except:
        print('Decryption Error!')
      print()
      pass
    elif choice == '4':
      break
    else:
      print()
      print('Invalid input. Exitting the program...')
      break


if __name__ == '__main__':
  main()
