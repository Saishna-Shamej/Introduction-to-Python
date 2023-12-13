#create class
class myclass:
    x = 5
#create object
p1 = myclass()
print(p1.x)
print()

#the init function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Mia", 25)

print(p1.name)
print(p1.age)
print()

#the str function
#without str
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)
#with str
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
      return f"{self.name}({self.age})"
p1 = Person('john', '29')
print(p1)
print()

#object methods
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello, my name is" + self.name)
p1 = person(" Mia", 28)
p1.myfunc()

#self parameter
class person:
    def __init__(today, name, age):
        today.name = name
        today.age = age
    def myfunc(ain):
        print("hello, my name is" + ain.name)
p1 = person(" Mia", 25)
p1.myfunc()
print()

'''#modify properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mia", 36)
p1.age = 40
print(p1.age)

#delete object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mia", 36)
p1.age = 40
del p1.age
print(p1.age)

#delete object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mia", 36)
p1.age = 40
del p1
print(p1.age)
print()

#pass statement
class person:
    pass'''