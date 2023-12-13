import re
txt = "The rain in the Spain"
x = re.findall("[arn]", txt) #check if the string has a, r, or n characters
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "The rain in the Spain"
x = re.findall("[a-n]", txt) #check if the strings has any characters between a and n
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "The rain in the Spain"
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "The rain in Spain"
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt) #check if the string has any two digits numbers from 00-59
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

import re
txt = "8 times before 11:45 AM"
x = re.findall("[+]", txt) #check if the string has any + characters
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

