import random

# Python implementation of the Miller-Rabin test according to the pseudocode at
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Pseudocode:~:text=prime%E2%80%9D%20otherwise-,let%20s%20%3E%200%20and%20d%20odd%20%3E%200%20such%20that%20n%20%E2%88%92%201,1%20then%0A%20%20%20%20%20%20%20%20return%20%E2%80%9Ccomposite%E2%80%9D%0Areturn%20%E2%80%9Cprobably%20prime%E2%80%9D,-Complexity%5Bedit
# n is the number to be tested; k is the number of testing rounds
def primality_test(n: int, k: int = 100) -> bool:
  if n <= 1:
    return False
  if n == 2 or n == 3:
    return True
  if n % 2 == 0:
    return False
  s = 0
  d = n - 1
  while d % 2 == 0:
    d //= 2
    s += 1
  for _ in range(k):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
      continue
    for _ in range(s - 1):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True

# Python implementation of the Extended Euclidean Algorithm according to the pseudoode at
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode:~:text=function%20extended_gcd(a,gcd%3A%22%2C%20(t%2C%20s)
# Returns a tuple (gcd, x, y) such that a * x + b * y = gcd, with gcd being the greatest common divisor of a and b.
def extended_gcd(a, b):
  old_r, r = a, b
  old_s, s = 1, 0
  old_t, t = 0, 1

  while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    old_t, t = t, old_t - quotient * t

  return (old_r, old_s, old_t)
