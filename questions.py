'''#string is a palindrome or not
a = "madam"
b = ""
for i in a:
    b = i + b
print(b)
if(a == b):
    print("The string is a palindrome")
else:
    print("The string is not palindrome")
print()

#python factorial program
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
print()

#natural numbers
for x in range(1, 11):
    print(x)
print()

#sum of digits

n = input("Enter number: ")
sum = 0
for num in str(n):
    sum = sum+int(num)
print(sum)
print()


#pattern
a = 0
for i in range(5, 0, -1):
    a = i
    for j in range(0, i):
        print(a, end=" ")
    print(" ")
print()

#value exists
x = range(1000)
y = int(input("Number : "))
if y in x:
    print("The number is present in range")
else:
    print("Don't exist")
print()'''

#largest of three numbers

a = int(input("first num : "))
b = int(input("sec number : "))
c = int(input("third num : "))
if a > b and a > c:
    print(" a is the largest number")
if b > c and b > a:
    print("b is the largest number")
if c > a and c > b:
    print("c is the largest number")
elif a == b == c:
    print("All are equal")
print()

