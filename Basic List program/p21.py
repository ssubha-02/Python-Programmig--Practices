my_list = [-10, -5, 0, 3, 7, -2, 8, -1]

positive_count = 0
negative_count = 0

for num in my_list:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Positive numbers count:", positive_count)  
print("Negative numbers count:", negative_count)  
