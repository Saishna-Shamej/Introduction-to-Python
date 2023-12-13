#current date and time
import datetime
x = datetime.datetime.now()
print(x)
print()

#current year
import datetime
x = datetime.datetime.now()
print(x.strftime('%Y'))
print()

#month of year
import datetime
x = datetime.datetime.now()
print(x.strftime('%B'))
print()

#day of month
import datetime
x = datetime.datetime.now()
print(x.strftime('%d'))
print()

#day of week
print(x.strftime('%A'))
print()


