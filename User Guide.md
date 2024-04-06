### Generating a new key-pair
Running `./generate.py` should print out n, e, and d. n and e are components of the public key, while d is the private key.

### Encrypting a string
Running `./encrypt.py text n e` should encrypt `text` and print out the encrypted string.

### Decrypting a string
Running `./decrypt.py text d n` should decrypt `text` and print out the decrypted string.

### Limitations
Due to the limited key size, the algorithm cannot correctly encrypt and decrypt strings exceeding certain lengths. To increase the length of supported strings, modify [generate.py](./generate.py) to increase the size of the generated keys.
