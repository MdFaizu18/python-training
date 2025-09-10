def is_spy(num):
    digits = [int(d) for d in str(num)]
    total_sum = 0
    total_product = 1

    for d in digits:
        total_sum += d
        total_product *= d

    return total_sum == total_product

print(is_spy(1124))  
print(is_spy(123))   
print(is_spy(125))   
