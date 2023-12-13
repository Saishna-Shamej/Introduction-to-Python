'''local scope'''


def myfunc():
    x = 300
    print(x)

myfunc()
print()

'''function inside function'''


def myfunc():
    x = 300
    def innerfunc():
        print(x)
        myinnerfunc()
myfunc()
print()

'''global scope'''

x = 300

def myfunc():
    print(x)
myfunc()
print(x)
print()

'''naming variables'''

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)
print()
'''global keyword'''

def myfunc():
    global x
    x = 200
myfunc()
print(x)
print()

x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)
print()
