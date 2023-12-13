import re
txt = "The rain in Spain"
x = re.findall("\AThe", txt) #check if the string starts with 'The'
print(x)
print()
#if statement can be added

x = re.findall("r\bain", txt) #check if "ain" is present in the beginning of a word
print(x)
print()

x = re.findall(r"ain\b", txt) #check if 'ain' present at the end of a word
print(x)
print()

x = re.findall(r"\Bain", txt) #check if 'ain' is present but not at the beginning of a word
print(x)
print()

x = re.findall(r"ain\B", txt) #check if 'ain' is present but not at the end of the word
print(x)
print()

x = re.findall("\d", txt) #check if the string contains any digit
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")
print()

x = re.findall("\D", txt) #return a match at every no digit character
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")
print()

x = re.findall("\s", txt) #return a match at every white space character
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")
print()

x = re.findall("\S", txt) #return a match at every non white space character
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")
print()

x = re.findall("\w", txt) #return a match at every word character( characters from a to z, digits from 0-9, and the underscore_character)
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")
print()

x = re.findall("\W", txt) #return a match at every non word character( characters not b/w a to z, like "!", "?", white space etc)
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")
print()

x = re.findall("Spain\Z", txt) #check if the string ends with "Spain"
print(x)
if x:
    print("There is atleast one match")
else:
    print("no match")

