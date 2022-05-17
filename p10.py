from datetime import datetime

print(datetime.now())
print(type(datetime.now()))

#datetime obj to str conversion
dat = datetime.now()
format = "%d %b %a %H:%M:%S"
# format = "%D %B %A %H:%M:%S"
print("date", dat.strftime(format)) #datetime class to string conversion