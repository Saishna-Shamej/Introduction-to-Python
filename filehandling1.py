'''f = open("filehandling.txt")
print()
f = open("filehandling.txt", "rt")
print()

f = open("filehandling.txt", "r")
print(f.read())
print()'''
#'''f = open("C:\Users\saish\PycharmProjects\class\file handling\fileHandling.txt", "r")
#print(f.read())'''
print()

'''f=open("fileHandling","r")
print(f.read(15))
print()'''

f = open("fileHandling.txt", "r")
print(f.readline())
print(f.readline())
print()
f = open("fileHandling.txt", "r")
for x in f:
    print(x)
print()
f = open("fileHandling.txt", "r")
print(f.readline())
f.close()