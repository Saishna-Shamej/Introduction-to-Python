"""single inheritance
multi level inheritance
multiple inheritance"""


class Family:
    def function1(self):
        print("hello")


class Person(Family):
    def function2(self):
        print("hii")


class Child(Person):
    def function3(self):
        print("Say hi")


obj = Child()
obj.function1()

print()


class Family:
    def function1(self):
        print("hello")


class School:
    def teachers(self):
        print("good morning")


class Students(Family, School):
    def function4(self):
        print("study")


abc = Students()
abc.teachers()
print()

#init function


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("MIYA", "KUMAR")
x.printname()

print()

