# 18) Smallest Missing Number (Advanced)

def smallest_missing(arr):
    arr.sort()
    target = 1
    for num in arr:
        if num <= target:
            target += num
        else:
            break
    print(target)

smallest_missing([1,2,10,12,13])