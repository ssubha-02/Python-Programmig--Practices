my_list = [3, 1, 4, 1, 5, 9, 2]

largest = second_largest = float('-inf')

for num in my_list:
    if num > largest:
        second_largest, largest = largest, num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)  
