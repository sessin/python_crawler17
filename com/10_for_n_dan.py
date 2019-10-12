# dan을 입력 받으면 해당 단을 출력하는 함수
def printNDan(dan):
    for num in range(1, 9 + 1):
        print(dan, "*", num, "=", dan * num, end="")

for dan in range(2, 9 + 1):
    print("-----" + str(dan) + "-----")
    printNDan(dan)








# 1 1 2 3 5 8 13


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 2) + fibo(n - 1)


def fibo2():
    first = 1
    second = 1
    third = 2
    for i in range(1, 10):
        third = first + second
        first = second
        second = third
