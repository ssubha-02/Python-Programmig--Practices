my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_remove = [2, 4, 6, 8]

for num in to_remove:
    if num in my_list:
        my_list.remove(num)

print(my_list) 