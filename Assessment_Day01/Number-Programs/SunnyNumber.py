import math

def is_sunny(num):
    return int(math.sqrt(num + 1)) ** 2 == num + 1

print(is_sunny(80))  
print(is_sunny(10))  
