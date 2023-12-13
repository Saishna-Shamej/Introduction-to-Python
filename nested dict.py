#dictionaries in dictionary

myfamily = {
    "child1" : {
    "name" : "emil",
    "year" : 2004
},
    "child2" : {
    "name" : "tobias",
    "year" : 2007
},
    "child3" : {
    "name" : "linus",
    "year" : 2011
    }
}
print(myfamily)
print()

#dictionaries to dictionary
child1 = {
    "name" : "emil",
    "year" : 2004
},
child2 = {
    "name" : "tobias",
    "year" : 2007
},
child3 = {
    "name" : "linus",
    "year" : 2011
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)
print()

#access items in nested dictionary

print(myfamily['child3']['name'])