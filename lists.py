thislist = ["apple", "orange", "cherry"]
print(thislist)
print()

print(thislist[0])
print()

print(thislist[-2])
print()

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])
print()

print(mylist[:6])
print()

print(mylist[1:])
print()

print(mylist[-4:-1])
print()

if "mango" in mylist:
  print("Yes, 'mango' is in the fruits list")
print()

mylist[1]="blackcurrent"
print(mylist)
print()

mylist[1:3]=["blackcurrant", "watermelon"]
print(mylist)
print()

thislist[1:2]=["blackcurrant", "watermelon"]
print(thislist)
print()

mylist=["apple", "banana", "cherry"]
mylist.insert(2,"watermelon")
print(mylist)
print()

mylist=["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)
print()

thislist=["apple", "banana", "cherry"]
tropical=["mango", "pineapple", "pappaya"]
thislist.extend(tropical)
print(thislist)
print()
tropical.append("orange")
print(tropical)
print()
thislist=["apple", "banana", "cherry"]
thistuple=("mango", "pineapple", "pappaya")
thislist.extend(thistuple)
print(thislist)
print()

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print()
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print()
thislist.pop()
print(thislist)
print()
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print()

del thislist
print(thislist)
print()

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)