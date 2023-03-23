import datetime
x=datetime.datetime.now()
print(x)

x=datetime.datetime(2006 ,6,6)
print(x)
print(x.strftime("%A"),x.strftime("%d"),x.strftime("%B"),x.strftime("%Y"))
