'''fruits = ["apple", "orange", "mango", "cherry", "pineapple"]
newlist= [x for x in fruits if x != "apple"]
print(newlist)'''
print()
fruits = ["apple", "orange", "mango", "cherry", "pineapple"]
newlist=[x for x in fruits]
print(newlist)
print()
newlist=[x for x in range(10)]
print(newlist)
print()
newlist=[x for x in range(10) if x<8]
print()
newlist=[x.upper() for x in fruits]
print(newlist)
print()
newlist=["2205" for x in fruits]
print(newlist)
print()
fruits = ["apple", "orange", "mango", "cherry", "pineapple"]
newlist=[x if x !="orange" else "sorry" for x in fruits]
print(newlist)
print()