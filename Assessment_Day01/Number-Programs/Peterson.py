import math

def is_peterson(num):
    return sum(math.factorial(int(d)) for d in str(num)) == num

print(is_peterson(145))  
print(is_peterson(123))  
