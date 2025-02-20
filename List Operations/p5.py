# Insert Items to a list

## Insert a Single Item at a Specific Index
my_list = [10, 20, 30, 40]

my_list.insert(2, 25)  # Insert 25 at index 2
print(my_list)

##Insert Multiple Items (Using Slicing)

my_list = [10, 20, 30, 40]

my_list[2:2] = [25, 26]  # Inserts 25 and 26 at index 2
print(my_list)



##Insert at the End (Same as append())
my_list = [10, 20, 30]
my_list.insert(len(my_list), 40)  # Insert 40 at the end
print(my_list)
