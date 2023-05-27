import datetime
now=datetime.datetime.now()
now=now.strftime('%Y-%m-%d %H-%M-%S')
print(now)
print(type(now))
filename=f"{now}.AVI"
print(filename)