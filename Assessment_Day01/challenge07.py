# 7) Product Perfect Square

import math

def perfect_square_product(n, m):
    product = n * m
    if int(math.sqrt(product)) ** 2 == product:
        print("yes")
    else:
        print("no")

perfect_square_product(5, 5)