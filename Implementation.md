### The general structure of the program.
\- [generate.py](./generate.py) contains the `generate() -> str` function that generates a pair of public and private keys.   
\- [encrypt.py](./encrypt.py) contains the `encrypt(text: str, n: int, e: int) -> str` function which encrypts a given string using the provided public key and returns the encrypted string.  
\- [decrypt.py](./decrypt.py) contains the `decrypt(text: str, d: int, n: int) -> str` function which decrypts a given string using the provided private key.  
\- [functions.py](./functions.py) contains the implementations of the Miller-Rabin primality test (`primality_test(n: int, k: int = 100)`) and the Extended Euclidean Algorithm (`extended_gcd(a: int, b: int) -> tuple[int, int, int]`).

### The time and space complexities achieved (e.g., Big O analyses from pseudocode).
\- `primality_test(n: int, k: int = 100)`, where $k$ is the number of testing rounds and n is the number to be tested:  
\+ Time complexity: $O(k \: log^3 n)$,  
\+ Space complexity: $O(log \: n)$  
\- `extended_gcd(a: int, b: int) -> tuple[int, int, int]`:  
\+ Time complexity: $O(log(min(a, \: b)))$  
\+ Space complexity: $O(log(max(a, \:  b)))$  
\- `generate() -> str`:  
\+ Time complexity: $O(k \: log^3 n)$,  
\+ Space complexity: $O(log \: n)$  
\- `encrypt(text: str, n: int, e: int) -> str`:  
\+ Time complexity: $O(log(e)*log^2 n )$  
\+ Space complexity: $O(log(max(n, \: e, \: t)))$, where $t$ is the size of the integer representing the original text  
\- `decrypt(text: str, d: int, n: int) -> str`:  
\+ Time complexity: $O(log(d)*log^2 n )$  
\+ Space complexity: $O(log \: n)$  

### Potential shortcomings and suggested improvements of the work.
\- `encrypt` and `decrypt` are sample proof-of-concept functions that only work for strings with quite limited sizes. Longer strings like a full essay or research paper might not be encrypted or decrypted as intended. This can be resolved by increasing the size of the generated keys, at the cost of the key generation taking more time.  
\- `encrypt` and `decrypt` currently only work for strings. They can be improved to work for entire files.  
\- Most of the code in this project is based on the most basic implementations of the algorithms involved. More optimisation to reduce time and space complexities can be carried out.

### Use of extensive language models (ChatGPT, etc.) State which model was used and how. Also, state if you have not used one. This is important!  
No LLM was used during the development of this project.
    
### References
**[1]** Wikipedia Contributors. 2024. RSA (cryptosystem). Wikipedia. [Online]. Available: [https://en.wikipedia.org/wiki/RSA_(cryptosystem)/](https://en.wikipedia.org/wiki/RSA_(cryptosystem)/). [Accessed: April 13, 2024].  
**[2]** Wikipedia Contributors. 2024. Miller–Rabin primality test. Wikipedia. [Online]. Available: [https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test/](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test/). [Accessed: April 13, 2024].  
**[3]** Wikipedia Contributors. 2024. Extended Euclidean algorithm. Wikipedia. [Online]. Available: [https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm/](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm/). [Accessed: April 13, 2024]. 
