# 15) Great Number

def great_number(n):
    digits = [int(d) for d in str(n)]
    m = sum(digits)
    j = 1
    for d in digits:
        j *= d
    print("Great" if m + j == n else "no")

great_number(59)