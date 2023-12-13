#create dictionary

student = {
    "first_name" : "Saishna",
    "last_name" : "Shamej",
    "Gender" : "Female",
    "Age" : 21,
    "Marital status" : "Single",
    "Skills" : ["Communication", "programming", "circuit setup"],
    "Country" : "India",
    "City" : "Thalasseery",
    "Address" : "Samanuaya(h), Kadirur"
}
print(student)
print()

#length of the dictionary
print(len(student))
print()

#get the value skills and check the data type
x = student["Skills"]
print(x)
print(type(x))
print()

#modify skills
x = student["Skills"]
print(x)
y = student["Skills"] = ["Adaptive",]
print(x + y)
print()

#get the dictionary keys as a  list
x = student.keys()
print(x)
print(list(x))
print()

#get the dictionary values as a list
x = student.values()
print(x)
print(list(x))
print()

#returning the dict as a list of tuples
y = student.items()
print(y)
print()

#delete one of the items
student.popitem()
print(student)
