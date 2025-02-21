from collections import Counter

list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 2, 4, 5, 6, 7, 8]

counter1 = Counter(list1)
counter2 = Counter(list2)

intersection = list((counter1 & counter2).elements())
print(intersection)
