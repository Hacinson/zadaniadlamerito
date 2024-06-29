list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

#elements in list1 but not in list2
difference1 = [item for item in list1 if item not in list2]

#elements in list2 but not in list1
difference2 = [item for item in list2 if item not in list1]

print("Difference (list1 - list2):", difference1)
print("Difference (list2 - list1):", difference2)
