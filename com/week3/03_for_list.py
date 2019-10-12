# list의 특징 for문을 이용해서 하나씩 꺼낼 수 있어요

# 빈 list를 return하는 getList라는 function을 만들고
# 콘솔에 []를 출력 해보세요
# 1 ~ 4가 들어있는 list를 return하게 고쳐보세요
# 1 ~ 10까지 들어있는 list를 return하게 고쳐보세요
# list안에 있는 모든 숫자에 getVAT()를 적용한 값이
# 출력되게 고쳐보세요

# getVAT함수는 money * 0.1을 return하는 함수 입니다.

def getVAT(money):
    return money * 0.1

def getList():
    list = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    for num in list:
        print(getVAT(num))
    return list

list = getList()

