# Split the array and add the first part to the end

def split_and_rotate(arr, d):
    d = d % len(arr)  
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotated_array = split_and_rotate(arr, d)
print("Rotated array:", rotated_array)
