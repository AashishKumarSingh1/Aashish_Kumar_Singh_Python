import datetime

dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")

print(dt)

print(dir(datetime))#used to know different methods availiable in the imported module.
# datetime.tzinfo

