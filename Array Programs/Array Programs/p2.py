# Find largest element in an array

def find_largest(arr):
    if not arr:
        return None  
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
arr = [3, 1, 7, 9, 2]
print("The largest element is",find_largest(arr))  
