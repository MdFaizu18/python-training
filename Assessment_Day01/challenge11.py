# 11) Smallest and Largest Index

def min_max_index(arr):
    smallest = min(arr)
    largest = max(arr)
    print(arr.index(smallest) + 1, arr.index(largest) + 1)

min_max_index([1, 2, 3, 4, 5])