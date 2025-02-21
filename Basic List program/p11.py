my_list = [123, 456, 789]

sum_of_digits = [sum(int(digit) for digit in str(num)) for num in my_list]

print(sum_of_digits)  