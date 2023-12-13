#empty tuple
thistuple = (" ", )
print(thistuple)
print()

#join fruits and vegetables tuple
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "beetroot", "potato")
tuple3 = fruits + vegetables
print(tuple3)
print()

#how many fruits youn have
fruits = ("apple", "banana", "cherry")
print(len(fruits))
print()

#add to fruits tuple
fruits = ("apple", "banana", "cherry")
y = list(fruits)
y.append("orange")
fruits = print(tuple(y))
print()

#slice out first 3 and last 3 from vegetables
vegetables = ("carrot", "beetroot", "potato", "spinach", "tomato", "cucumber", "onion")
print(vegetables[2:-3])
print()

#delete veg tuple completely
vegetables = ("carrot", "beetroot", "potato")
del(vegetables)
print(vegetables)

