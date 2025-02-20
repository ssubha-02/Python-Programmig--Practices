# Program for array rotation

def rotate_array(arr, d):
    n = len(arr)
    d = d % n  
    rotated = arr[d:] + arr[:d]
    return rotated


arr = [1, 2, 3, 4, 5]
d = 2
print("Original array:", arr)
print("Rotated array:", rotate_array(arr, d))
