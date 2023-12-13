#lambda function to add 2 numbers
x = lambda a, b : a + b
print(x(5, 8))
print()

#check if number is even using lambda
x = lambda a : "Even number" if a % 2 == 0 else "Odd number"
print(x(4))
print()

#lamda function to calculate factorial of a number
x = lambda b : 1 if b <= 1 else b*x(b-1)
number = int(input('num = '))
print(x(number))
print()
'''
#filter even numbers from a list
lis = [2, 9, 5, 1, 8, 6, 7, 4, 3, 10]
even = lambda x : x % 2 ==0
print(list(even))
print()'''

#lambda function to reverse a string
x = lambda a : str(a)[::-1]
y = str(input('str = '))
print(x(y))
print()