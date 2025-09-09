# 12) GCD of Two Numbers
import math

def gcd(n, m):
    if n == 0 or m == 0:
        print(-1)
    else:
        print(math.gcd(n, m))

gcd(10, 5)