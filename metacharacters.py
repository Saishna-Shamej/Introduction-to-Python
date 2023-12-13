#1
import re
txt = "The rain in spain"
x = re.findall("[a-m]", txt)
print(x)
print()
#2
import re
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)
print()
#3
x = re.findall("do...rs", txt)
print(x)
print()
#4
x = re.findall("^That", txt)
if x:
    print("Yes, the string starts with 'that' ")
else:
    print("No match")
print()
#5
x = re.findall("dollars$", txt)
if x:
    print("Yes, the string ends with 'dollars' ")
else:
    print("No match")
print()
#6 zero or more occurances
import re
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)
print()
#7 one or more occurances
import re
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)
print()
#8 zero or one occurances
import re
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)
print()
x = re.findall("he.{2}o", txt)
print(x)
print()

#9  either or
import re
txt = "the rain in spain falls mainly in the plain"
x = re.findall("falls|stays", txt)
print(x)
if x:
    print("there is atleast one match")
else:
    print("no match")