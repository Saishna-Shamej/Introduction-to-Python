x = lambda a : a + 10
print(x(5))
print()

x = lambda a, b : a * b
print(x(4,3))
print()

x = lambda a, b, c : a + b + c
print(x(4, 5, 9))
print()

def myfunc(n):
    return lambda a : a * n
mytri = myfunc(3)
print(mytri(22))
print()

def myfunc(n):
    return lambda a : a * n
mydou = myfunc(2)
print(mydou(4))
print()

def myfunc(n):
    return lambda a  : a * n
mydou = myfunc(2)
mytri = myfunc(3)
print(mydou(23))
print(mytri(54))
print()