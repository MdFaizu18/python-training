# 22) Beautiful Array

def is_beautiful(arr):
    total = sum(arr)
    print(1 if total % 2 == 0 and total % 3 == 0 and total % 5 == 0 else 0)

is_beautiful([5, 25, 35, -5, 30])