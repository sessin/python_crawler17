# 구구단 2단을 출력하는 함수를 만들어 보세요
def print2Dan():
    for num in range(1, 9 + 1):
        print(2, "*", num, "=", 2 * num)
print2Dan()

def print3Dan():
    for num in range(1, 9 + 1):
        print(3, "*", num, "=", 3 * num)
print3Dan()

# 2단, 3단
# 2단 3단 동시에 출력
# 2단 100단
print2Dan()
print3Dan()
