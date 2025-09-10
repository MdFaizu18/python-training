def tech_number(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    first_half = int(s[:half])
    second_half = int(s[half:])
    return (first_half + second_half) ** 2 == num

print(tech_number(3025))  # True
print(tech_number(2025))  # True
print(tech_number(1312))  # False
