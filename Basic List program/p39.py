my_list = [10, 20, 5, 30, 15, 5, 30]

max_value = max(my_list)
min_value = min(my_list)

max_positions = [i for i, v in enumerate(my_list) if v == max_value]
min_positions = [i for i, v in enumerate(my_list) if v == min_value]

print(f"Maximum element at indices: {max_positions}")
print(f"Minimum element at indices: {min_positions}")
