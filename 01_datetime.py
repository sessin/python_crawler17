import datetime
import random

now = datetime.datetime.now()

file = open("./log.txt", "w+")
for i in range(30):
    now += datetime.timedelta(seconds=10)
    file.write("{},{}\n".format(now,random.randint(1, 10)))
file.close()
