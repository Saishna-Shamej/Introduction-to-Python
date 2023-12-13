#create a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)
print()

#add members
thisset = {'cherry', 'apple', 'banana'}
thisset.add("orange")
print(thisset)
print()

#remove item
thisset = {'cherry', 'apple', 'banana', 'orange'}
thisset.remove("orange")
print(thisset)
print()

#remove an item that doest exist
thisset = {'cherry', 'apple', 'banana'}
thisset.discard("orange")
print(thisset)
print()

#create intersection of sets
x = {'cherry', 'apple', 'banana'}
y = {'apple', 'orange', 'pineapple'}
z = x.intersection(y)
print(z)
print()

#create union of sets
x = {'me', 'mine', 'myself'}
y = {1, 2, 3}
z = x.union(y)
print(z)
print()

#create set difference
x = {'cherry', 'apple', 'banana'}
y = {'apple', 'orange', 'pineapple'}
z = x.difference(y)
n = y.difference(x)
print(n)
print(z)
print()

#create symmetric difference
x = {'cherry', 'apple', 'banana'}
y = {'apple', 'orange', 'pineapple'}
z = x.symmetric_difference(y)
print(z)
