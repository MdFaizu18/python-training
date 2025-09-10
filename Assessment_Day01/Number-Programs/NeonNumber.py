def is_neon(num):
    sq = num * num
    return sum(int(d) for d in str(sq)) == num

print(is_neon(9))   
print(is_neon(45))  
print(is_neon(12))  
