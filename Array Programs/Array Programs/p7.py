# Check if given array is Monotonic

def is_monotonic(arr):
    increasing = decreasing = True
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:  
            decreasing = False  # Not non-increasing
        if arr[i] < arr[i - 1]:  
            increasing = False  # Not non-decreasing

    return increasing or decreasing

# Example usage:
arr1 = [1, 2, 2, 3] 
arr2 = [6, 5, 4, 4] 
arr3 = [1, 3, 2]    

print(is_monotonic(arr1))  
print(is_monotonic(arr2))  
print(is_monotonic(arr3)) 
