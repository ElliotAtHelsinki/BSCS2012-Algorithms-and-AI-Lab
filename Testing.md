### The coverage report of the unit tests.
```
Name                           Stmts   Miss  Cover
--------------------------------------------------
test/__init__.py                   0      0   100%
test/test_eea.py                 105      1    99%
test/test_encrypt_decrypt.py      18      1    94%
test/test_generator.py            14      1    93%
test/test_primality_test.py       51      1    98%
--------------------------------------------------
TOTAL                            188      4    98%
```

### What has been tested and how?
\- The Extended Euclidean Algorithm has been tested to make sure that given `a` and `b`, it correctly returns a tuple `(gcd, x, y)` such that `a * x + b * y = gcd`, with `gcd` being the greatest common divisor of `a` and `b`. The following cases were tested:  
\+ Both `a`, `b` are positive integers.  
\+ Either `a` or `b` is zero.  
\+ Both `a` and `b` are zero.  
\+ Either `a` or `b` is negative, the other is positive.  
\+ Both `a` and `b` are negative integers.  
\- The implementation of the Miller-Rabin primality test has been tested. The implementation correctly works as the test theoretically envisioned. The test is only probabilistic, so it might occassionally mistake a composite number as a prime. However, for our purposes, it is good enough.  
\- The key generator has been tested to make sure it correctly returns the public key components n and e as well as the private key d.  
\- The encrypt and decrypt functions have been tested to make sure that:  
\+ The encrypted string is not the same as the original string.  
\+ The decrypted string is the same as the original string.  
    
### What kind of inputs were used for the testing?
\- For the Extended Euclidean Algorithm, we inputted different values of `a` and `b`.  
\- For the Miller-Rabin test, we inputted some prime numbers, non-prime numbers, as well as edge cases.  
\- For the key generator, no input is required.  
\- For the encrypt and decrypt functions, we inputted a few sample strings in several different languages.  

### How can the tests be repeated?
Running `./coverage.sh` on the terminal should execute all the written tests. New tests can also be written to the files inside the [test](./test) folder.  
