# Find sum of array

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [1, 2, 3, 4, 5]
print("Sum of Array is:",array_sum(arr)) 


# Using builtin function

arr = [1, 2, 3, 4, 5]
total = sum(arr)
print(total)  

