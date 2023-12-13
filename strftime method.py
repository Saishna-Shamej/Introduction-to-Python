import datetime
x = datetime.datetime(2018, 8, 3, )
print(x.strftime('%B')) #month
print(x.strftime('%b')) #month in short version
print(x.strftime('%w')) #weekday as number sunday is 0
print(x.strftime('%d')) #day
print(x.strftime('%m')) #month as number
print(x.strftime('%y')) #year without century
print(x.strftime('%Y')) #year full version
print()


import datetime
x = datetime.datetime.now()
print(x.strftime('%H')) #hour 00-23
print(x.strftime('%I')) #hour 00-12
print(x.strftime('%p')) #AM-PM
print(x.strftime('%M')) #minute 00-59
print(x.strftime('%S')) #second 00-59
print(x.strftime('%f')) #microsecond 000000-999999
print(x.strftime('%z')) #UTC offset
print(x.strftime('%Z')) #timezone
print(x.strftime('%j')) #day number of year 001-366
print(x.strftime('%U')) #week number of year , sunday as the first dayof the week, 00-53
print(x.strftime('%W')) #eek number of year , monday as the first dayof the week, 00-53
print(x.strftime('%c')) #local version of time and date
print(x.strftime('%C')) #century
print(x.strftime('%X')) #local version of time
print(x.strftime('%x')) #local version of date
print(x.strftime('%%')) #A% character
print(x.strftime('%G')) #ISO 8601 YEAR
print(x.strftime('%u')) #iso 8601 weekday(1-7)
print(x.strftime('%V')) #iso 8601 weeknumber(01-53)
