thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :2003
}
print(thisdict)
print()
print(thisdict["brand"])
print()

#no duplicates allowed
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 2003,
    "year" : 2005
}
print(thisdict)
print()
print(len(thisdict))
print()

#can be of any data types
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 2005,
    "colour" : ["red", "white", "blue", "black"],
    "electric" : False
}
print(thisdict)
print()
print(type(thisdict))
print()

#dict constructer

thisdict = dict(Name= "John", Age = 40, Country = "Australia")
print(thisdict)
print()