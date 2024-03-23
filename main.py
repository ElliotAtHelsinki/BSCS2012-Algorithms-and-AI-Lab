import secrets
import math
from functions import primality_test, extended_gcd

# Step 1: Find two large prime number p and q such that their produce has length of at least 1024 bits.
p = None
q = None

# p*q will certainly be at least 1024 bits long if p and q are 1024 bits long each.
# Therefore, we shall generate random 1024-bit integers and test them until we get two suitable prime numbers.
while p == None:
  random_number = secrets.randbits(1024)
  if primality_test(random_number):
    p = random_number

while q == None:
  random_number = secrets.randbits(1024)
  if primality_test(random_number) and p != random_number:
    q = random_number

# Step 2: Compute n = pq
n = p * q

# Step 3: Compute λ(n)
delta_n = math.lcm(p - 1, q - 1)

# Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.
e = 65537

# Step 5: Determine d as d ≡ e^(-1)(mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n).
_, x, _ = extended_gcd(e, delta_n)
d = x % delta_n

print(f'n: {n}')
print(f'e: {e}')
print(f'd: {d}')
