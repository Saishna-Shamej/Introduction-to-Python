#using a module

import mymodule
mymodule.greeting('Jonathan')
print()

#variables in module

import mymodule
a = mymodule.person1["Country"]
print(a)
print()

#renaming a module

import mymodule as mx
a = mx.person1["Age"]
print(a)
print()

#built-in modules
import platform
x = platform.system()
print(x)
print()

import calendar
y = 2023
m = 4
x = calendar.month(y, m)
print(x)

#using dir() function

import platform
x = dir(platform)
print(x)
print()

import calendar
x = dir(calendar)
print(x)
print()

'''import from module using from keyword'''

from mymodule import person1
print(person1["Country"])