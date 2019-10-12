
#for i in range(2, 9 + 1):
#    for j in range(1, 9 + 1):
#        print("{} * {} = {}".format(i, j, i * j))

def printNDan(dan):
    for num in range(1, 9 + 1):
        print(dan, "*", num, "=", dan * num)

for dan in range(2, 9 + 1):
    print("----{}----".format(dan))
    printNDan(dan)
