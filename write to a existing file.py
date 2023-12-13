'''f = open("fileHandling.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
print()
f = open("fileHandling.txt", "r")
print(f.read())
print()

f = open("myfile.txt", "x")
f = open("myfile.txt", "w")
print()
'''
#delete file
#f = open("file3.txt", "x")
#import os
#os.remove("file3.txt")

#check if file exist
import os
if os.path.exists("fileHandling.txt"):
  os.remove("fileHandling.txt")
else:
  print("The file does not exist")

  #to delete entire folder

#import os
#os.rmdir("myfile")