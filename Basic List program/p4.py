my_list = [1, 2, 3, 4, 5]

first = my_list.pop(0)  
last = my_list.pop(-1)  

my_list.insert(0, last)  
my_list.append(first)  

print(my_list)  
