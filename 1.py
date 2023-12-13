cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
cars.append("Honda")
print(cars)
cars.pop(1)
print(cars)
cars.remove("Honda")
print(cars)
cars.clear()
print(cars)
print()
cars = ["Ford", "Volvo", "BMW"]
x = cars.copy()
print(x)
print()
x = cars.count("Volvo")
print(x)
print()

y = [1, 2, 3]
cars.extend(y)
print(cars)
print()
x = cars.index("Volvo")
print(x)
print()
cars.insert(2, "Kia")
print(cars)
print()
cars.reverse()
print(cars)
print()
cars = ["Ford", "Volvo", "BMW"]
cars.sort()
print(cars)
cars.sort(reverse = True)
print()

def myfunc(i):
    return(i)
cars = ["Ford", "Volvo", "BMW"]
cars.sort(key = myfunc)
print(cars)
print()

def myfunc(i):
    return i['year']
cars = [
    {'car' : 'Ford', 'year' : 2009},
    {'car' : 'BMW', 'year' : 2003},
    {'car' : "Volvo", "year" : 2011}
]
cars.sort(key = myfunc)
print(cars)
print()

def myfunc(i):
    return(i)
cars = ["Ford", "Volvo", "BMW"]
cars.sort(reverse = True, key = myfunc)
print(cars)