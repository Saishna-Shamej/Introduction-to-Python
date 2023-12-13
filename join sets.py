#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print()

#update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
print()

#keep only duplicates
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3, 4}
set1.intersection_update(set2)
print(set1)
print()

#duplicate alone to new set
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3, 4}
set3 = set1.intersection(set2)
print(set3)
print()

#keep all but no duplicates
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)
print()

#no duplicates to new set
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3, 4}
set3 = set1.symmetric_difference(set2)
print(set3)
print()

#True and 1 are considered same
set1 = {"a", "b", "c", True, False}
set2 = {1, 2, 3, 4, 5, "google", "mine"}
set3 = set1.symmetric_difference(set2)
print(set3)
print()