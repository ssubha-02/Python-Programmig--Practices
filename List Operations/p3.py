# Replace Values in a List in Python

##Replace a Single Value (Using Indexing)
my_list = [10, 20, 30, 40, 50]

my_list[1] = 99  # Change 20 to 99
print(my_list)

##Replace Multiple Values (Using Slicing)
my_list = [10, 20, 30, 40, 50]

my_list[1:3] = [99, 88]  # Replacing 20 and 30 with 99 and 88
print(my_list)

##Replace All Occurrences of a Value (Using List Comprehension)my_list = [10, 20, 30, 20, 50]

my_list = [99 if x == 20 else x for x in my_list]  # Replace all 20s with 99
print(my_list)

