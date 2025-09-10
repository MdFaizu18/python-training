def is_duck(num):
    s = str(num)
    return not s.startswith("0") and "0" in s

print(is_duck(3210))   
print(is_duck(7033))   
print(is_duck(08237))  
