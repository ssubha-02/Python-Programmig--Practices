def find_duplicates(lst):
    count = {}
    duplicates = set()

    for num in lst:
        count[num] = count.get(num, 0) + 1
        if count[num] > 1:
            duplicates.add(num)

    return list(duplicates)

my_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1, 9, 10, 3]
print(find_duplicates(my_list))  