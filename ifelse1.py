a = 22
b = 220
if a > b:
   print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")
print()

#short hand if
a = 220
b = 39
if a > b: print("a is greater than b")
print()

#short hand if else
a = 220
b =39
print ("A") if b>a else print("B")
print()
#technique is called  Ternary Operators, or Conditional Expression

#multiple conditions in one statement
a = 220
b = 220
print("A") if a > b else print("=") if a == b else print("B")
print()

#AND
a = 456
b = 234
c = 23
if a > b and b > c:
    print("both conditions are true")
print()

#OR
a = 456
b = 234
c = 23
if a > b or c > a:
    print("atleast one of the conditiona are true")
print()

#NOT
a = 456
b = 234
c = 23
if not b > a:
    print("b is not greater than a")
print()

#NESTED IF
x = 2

if x > 10:
    print("Above 10")
    if x < 20:
        print("also above 20")
else:
        print("but not above 20")
print()


#PASS
a = 80
b = 40
if a < b:
    pass