# Reversal algorithm for array rotation

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    n = len(arr)
    d = d % n  
    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse the remaining elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse the whole array
    reverse(arr, 0, n - 1)

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotate_array(arr, d)
print("Rotated array:", arr)
