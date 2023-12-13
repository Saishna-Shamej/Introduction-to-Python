for i in range(6):
    for j in range(i + 1):
        print('*', end="  ")
    print()
print()

for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print('*', end="  ")
    print()
#natural numbers
for i in range(6):
    for j in range(i):
        print(i, end=" ")
    print(" ")
    print()

#odd numbers
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i * 2 - 1, end=" ")
        j = j + 1
    i = i + 1
    print()
print()

#even numbers
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i * 2, end=" ")
        j = j + 1
    i = i + 1
    print()

print()

#reverse a number
x = 3456
y = str(x)[::-1]
print(y)
