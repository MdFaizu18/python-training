# 16) Max Frequency Digit

def max_frequency(arr):
    max_count = 0
    result = arr[0]
    for num in arr:
        count = arr.count(num)   
        if count > max_count:    
            max_count = count
            result = num
    print(result)

max_frequency([1, 2, 3, 4, 4, 4, 5])
