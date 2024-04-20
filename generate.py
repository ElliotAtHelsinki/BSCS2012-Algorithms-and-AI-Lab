#!/usr/bin/python
import math

from functions import primality_test
from functions import extended_gcd
from Cryptodome.Random.random import getrandbits


def generate() -> tuple[int, int, int]:
  # Step 1: Find two large prime number p and q such that their produce has length of at least 1024 bits.
  p = None
  q = None

  # p*q will certainly be at least 1024 bits long if p and q are at least 1024 bits long each.
  while p == None:
    num_bits = 2048
    random_number = getrandbits(num_bits - 1) | (1 << (num_bits - 1))  # Generate 2047 random bits and add an additional 1-bit to the left to create a random 2048-bit integer
    if random_number >= 2**1023 and primality_test(random_number):
      p = random_number

  while q == None:
    num_bits = 2048
    random_number = getrandbits(num_bits - 1) | (1 << (num_bits - 1))
    if random_number >= 2**1023 and primality_test(random_number) and p != random_number:
      q = random_number

  # Step 2: Compute n = p * q
  n = p * q

  # Step 3: Compute λ(n)
  delta_n = math.lcm(p - 1, q - 1)

  # Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.
  e = 65537

  # Step 5: Determine d as d ≡ e^(-1)(mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n).
  _, x, _ = extended_gcd(e, delta_n)
  d = x % delta_n

  return (n, e, d)


def main():
  (n, e, d) = generate()
  print(f'n: {n}')
  print(f'e: {e}')
  print(f'd: {d}')


if __name__ == '__main__':
  main()
