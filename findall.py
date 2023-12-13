import re
txt = "The rain in spain"
x = re.findall("ai", txt)
print(x)
print()
x = re.findall("India", txt)
print(x)
print()
if (x):
    print("There is atleast one match")
else:
    print("No match")
print()

#search function

import re
txt = "the rain in spain"
x = re.search("\s", txt)
print("the first white space character is located in position:", x.start())
print()

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
print()


#split function
import re
txt = "the rain in spain"
x = re.split("\s", txt)
print(x)
print()

import re
txt = "the rain in spain"
x = re.split("\s", txt, 2)
print(x)
print()

#sub function
import re
txt = "the rain in spain"
x = re.sub("\s", "9", txt)
print(x)
print()

import re
txt = "the rain in spain"
x = re.sub("\s", "9", txt, 2)
print(x)

