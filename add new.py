#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print()

#add another set
thisset = {"apple", "banana","cherry"}
tropical = {"pineapple", "guava", "grape"}
thisset.update(tropical)
print(thisset)
print()

#add iterable
thisset = {"apple","banana", "cherry"}
mylist = ["me", "mine"]
thisset.update(mylist)
print(thisset)
print()

#remove items
thisset = {"apple","banana", "cherry"}
thisset.remove("cherry")
print(thisset)
print()

#discard method
thisset = {"apple","banana", "cherry"}
thisset.discard("cherry")
print(thisset)
print()

#random removal
thisset = {"apple","banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #set after removal of item
print()

#empties set
thisset = {"apple","banana", "cherry"}
thisset.clear()
print(thisset)
print()

#delete set
thisset = {"apple","banana", "cherry"}
thisset.del()
print(thisset)
print()