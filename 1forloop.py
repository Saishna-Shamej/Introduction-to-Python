fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print()

#looping through a string
for x in "banana":
    print(x)
print()

#break statement 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print()

#break statement 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print()

#continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print()

#range function
for x in range(9):
    print(x)
print()

for x in range(2,6):
    print(x)
print()

for x in range(3, 20, 2):
    print(x)
print()

#else in for loop
for x in range(9):
    print(x)
else:
    print("finally finished")
print()

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
print()

#pass statement
for x in [0, 1, 6]:
    pass