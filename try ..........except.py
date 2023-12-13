'''try:
  print(x)
except:
  print("An exception occurred")
print()

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#here try block raises name error and another for other errors
print()

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#try block doesnot arise any errors else statements works
print()

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#finally block if specified will be executed regardless if the try block raises an error or not
print()

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong whe  writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
#try block raises an error while trying to write a read only file
print()

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
print()'''


x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")