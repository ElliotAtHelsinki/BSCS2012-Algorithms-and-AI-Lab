### Degree programme:
Bachelor's Programme in Science

### What programming language are you using?
Python

### Also, mention any other languages you are proficient in to the extent that you can peer review projects made in them if necessary:
JavaScript, TypeScript

### What algorithms and data structures are you implementing in your work?
The Miller-Rabin test is implemented to check the primality of numbers. In addition, the Extended Euclidean Algorithm is implemented to compute the greatest common divisor of two integers as well as coefficients of Bézout's identity. No significantly advanced data structures are needed, so far.

### What problem are you solving?
Producing an implementation of RSA encryption capable of producing keys of at least 1024 bits, according to the specification at [https://en.wikipedia.org/wiki/RSA_(cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

### What inputs does your program take, and how are these used?
A basic implementation of RSA key generation has been developed so far, and this requires no input. Executing main.py with no arguments simply prints out the randomly generated keys, including:
\- The public key: This includes the modulus `n` and the public exponent `e`.
\- The private key: This is the private exponent `d`.

There are two additional functions:
\- `encrypt(text: str, n: int, e: int) -> str`: Encrypts a given string using the provided public key and returns the encrypted string
\- `decrypt(text: str, d: int) -> str`: Decrypts a given string using the provided private key.
