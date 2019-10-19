# 빈 list를 선언하고 출력 해보세요

# 빈 list를 return하는 함수를 만들고 list를 출력 해보세요

# 1,2,3이 들어있는 list를 리턴하는 함수로 바꿔보세요

# matthew, mark, luke, john이 들어있는 list를 return하는
# 함수로 바꿔보세요

# 이름의 두번째 글자를 출력 해보세요.
# a
# a
# u
# o

# extract python nth char

def getList():
    list = ["matthew", "mark", "luke", "john"]
    for name in list:
        print(name[1])
    return list

result = getList()
print(result)

