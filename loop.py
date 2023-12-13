thislist=["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print()

for x in range(len(thislist)):
    print(thislist[x])
print()

thislist=["apple", "banana", "mango", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

print()


#list comprehension

thislist=["apple", "orange", "mango","cherry","kiwi"]
[print(x) for x in thislist]
print()

'''newlist=[x for x in thislist if "a" in x]
print(newlist)
print()'''

newlist=[x for x in thislist if "g" in x ]
print(newlist)
print()
