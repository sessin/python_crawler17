# 2 ~ 10까지 반복문으로 짝수를 출력하는 함수를 만들어 보세요
# case1
def printEven():
    for num in range(10, 20 + 1):
        print(num * 2)
printEven()
print("------------")

def printEven2():
    for num in range(2, 11, 2):
        print(num)
printEven2()

print("------3------")
def printEven3():
    for num in range(1, 11):
        if num % 2 != 0:
            print(num)

printEven3()