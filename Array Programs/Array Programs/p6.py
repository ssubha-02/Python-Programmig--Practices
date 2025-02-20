# Find reminder of array multiplication divided by n

def find_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n 
    return result

arr = [3, 4, 5]
n = 7
print("Remainder:", find_remainder(arr, n))
