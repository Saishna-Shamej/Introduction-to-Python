
#generator function
def function_name():
    yield statement

print()

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
for value in simpleGeneratorFun(): #driver code to check above generator function
    print(value)
print()

#generator object
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
x = simpleGeneratorFun() #x is a generator object
#iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))
print()

#generator expression
generator_exp = (i*5 for i in range(10) if i%2 == 0)
for i in generator_exp:
    print(i)


