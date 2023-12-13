thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
x = thisdict["model"]
print(x)
print()
x = thisdict.get('brand')
print(x)
print()
x = thisdict.keys()
print(x)
print()

#add new item to the original dictionary
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
x = car.keys()
print(x)  #before change
print()
car["colour"] = "White"
print(x) #after change
print()
x = thisdict.values()
print(x)
print()

#make change in original dictionary
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
x = car.values()
print(x)  #before change
print()
car["year"] = 2005
print(x)  #after change
print()

#get item
x = car.items()
print(x)
print()

#change items
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
x = car.items()
print(x)  #before change
car["model"] = "fiesta"
print(x)  #after change
print()
#item list updation

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
x = thisdict.items()
print(x) #before change
thisdict["colour"] = "red"
print(x)  #after change
print()

#check if key exists
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")

    #change items and update dictionaries are same as above methods
    
