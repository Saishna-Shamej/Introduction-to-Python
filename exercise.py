#greeting message
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = person("MIYA", 25)
p1.myfunc()
print()

#class car
class car:
    def __init__(self, colour, model, year):
        self.colour = colour
        self.model = model
        self.year = year
    def myfunc(self):
        return f"{self.model} ({self.colour}) ({self.year})"
c1 = car("Ford", "white", 2011)
print(c1.myfunc())
print()

#class book
class books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def myfunc(self):
        return f"{self.title} ({self.author}) ({self.year})"
b1 = books("abc", "xyz", 2002)
print(b1.myfunc())
print()

#class circle
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return f"{self.radius*self.radius*3.14}"
b1 = circle(5)
print(b1.area())
print()

#class rectangle
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        return f"{2*(self.length+self.breadth)}"
r1 = rectangle(4, 7)
print(r1.perimeter())
print()