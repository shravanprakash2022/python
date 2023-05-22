my_set = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
check = 10 in my_set
print(check)


my_set.add(19)
my_set.remove(9)
my_set1 = {1, 4, 6, 5, 9, 0, 8, 3, 2, 7, 11}
my_set2 = {12, 9, 4, 2, 0, 6}
common = my_set1.intersection(my_set2)
#print(sorted(list(common)))
print(common)
join = my_set1.union(my_set2)
print(join)
diff = my_set2.difference(my_set1)
print(diff)