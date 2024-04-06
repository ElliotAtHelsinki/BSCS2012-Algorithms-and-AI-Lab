### The coverage report of the unit tests.
```
Name                           Stmts   Miss  Cover
--------------------------------------------------
decrypt.py                        21     11    48%
encrypt.py                        16      9    44%
functions.py                      34      0   100%
generate.py                       28      5    82%
test/__init__.py                   0      0   100%
test/test_eea.py                  29      1    97%
test/test_encrypt_decrypt.py      17      1    94%
test/test_generator.py            12      1    92%
test/test_primality_test.py       23      1    96%
--------------------------------------------------
TOTAL                            180     29    84%
```

### What has been tested and how?
\- The Extended Euclidean Algorithm has been tested to make sure that given a and b, it correctly returns a tuple (gcd, x, y) such that a * x + b * y = gcd, with gcd being the greatest common divisor of a and b. The following cases were tested:
\+ a, b are both positive integers.
\+ Either a or b is zero.
\+ Both a and b are zero.
\+ Either a or b is negative, the other is positive.
\- The implementation of the Miller-Rabin primality test has been tested. The implementation correctly works as the test theoretically envisioned. The test is only probabilistic, so it might occassionally mistake a composite number as a prime. However, for our purposes, it is good enough.
\- The key generator has been tested to make sure it correctly returns the public key components n and e as well as the private key d.
\- The encrypt and decrypt functions have been tested to make sure that:
\+ The encrypted string is not the same as the original string.
\+ The decrypted string is the same as the original string.
    
### What kind of inputs were used for the testing?
\- For the Extended Euclidean Algorithm, we inputted different values of a and b.
\- For the Miller-Rabin test, we inputted some prime numbers, non-prime numbers, as well as edge cases.
\- For the key generator, no input is required.
\- For the encrypt and decrypt functions, we inputted a sample string: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`

### How can the tests be repeated?
Running `./coverage.sh` on the terminal should execute all the written tests. New tests can also be written to the files inside the [test](./test) folder.
