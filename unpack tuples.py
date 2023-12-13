#unpacking a tuple
fruits = ("apple", "banana", "Cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

#using astrick*
fruits = ("apple", "banana", "cherry", "Strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print()

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
print()


