#alphabetically

'''thislist = ["apple", "mango", "kiwi", "pineapple", "banana", "carrot"]
thislist.sort()
print(thislist)
print()
thislist.sort(reverse = True)
print(thislist)
print()

#numerically
print()
thislist = [41, 66, 25, 69, 88, 36, 40, 20, 17, 28]
thislist.sort()
print(thislist)
print()
thislist.sort(reverse = True)
print(thislist)
print()
thislist=["banana", "Orange", "Cherry", "kiwi"]
thislist.sort()
print(thislist)
print()'''

'''thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.sort(key = str.lower)
print(thislist)
print()'''
thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.reverse()
print(thislist)
print()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print()
mylist = list(thislist)
print(mylist)
print()
list1 = ["me", "myself", "mine"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list3)
print()
'''for x in list2:
    list1.append(x)
print(list1)
print()'''
list1.extend(list2)
print(list1)
print()

