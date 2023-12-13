#creating a function
def my_function():
    print("hello from a function")
print()

#calling a function
def my_function():
    print("hello from a function")
my_function()
print()

#arguments
def my_function(fname):
    print(fname + " Shamej")
my_function("Saishna")
my_function("Sayona")
my_function("Sabina")
print()

#number of arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Saishna", "Shamej")
print()

#if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
#If you try to call the function with 1 or 3 arguments, you will get an error:
#example
'''def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Saishna")
print()'''

#arbitary arguments *args
def my_function(*kids):
    print("the youngest child is"+ kids[1])
my_function(" Saishna", " Sayona")
print()

#keyword arguments
def my_function(child2, child1):
    print("the youngest child is" + child2)
my_function(child1 = " Saishna", child2 = " Sayona")
print()

#arbitary keyword arguments **kwargs
def my_function(**kid):
    print("his last name is" + kid["lname"])
my_function(fname = "Saishna", lname = " Shamej")
print()

#default parameter values
def my_function(country = ' Norway'):
    print("I'm from" + country)
my_function(" sweden")
my_function(" India")
my_function()
my_function(" Australia")
print()

#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ['apple', 'banana', 'cherry']
my_function(fruits)
print()

#return values
def my_function(x):
    return 6 * x
print(my_function(6))
print(my_function(5))
print(my_function(2))
print()

#pass statement
def my_function():
    pass
print()

#recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6))