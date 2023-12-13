age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 5
itemno = 600
price = 50
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 5
itemno = 600
price = 50
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))