#change tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "orange"
x = tuple(y)
print(x)
print()
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("kiwi")
thistuple = tuple(y)
print(thistuple)
print()

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
print()
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)
print()
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
print()
