my_list = [1, None, 2, None, 3, 4, None, 5]

filtered_list = list(filter(lambda x: x is not None, my_list))
print(filtered_list)
