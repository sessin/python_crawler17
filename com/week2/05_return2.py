# shift + f6 이름바꾸기

def plus(val1, val2):
    return val1 + val2

# minus함수를 만들고 10 - 20을 구해보세요
# multiple, divide 10 * 20, 10 / 20
result = plus(10, 20)
print(result)

multiple = lambda x, y: x * y
divide = lambda x, y: x / y
minus = lambda x, y: x - y


# 위에서 만든 함수를 조합하여
# (10 * 20) - (30 / 40)를 구해보세요
result1 = multiple(10, 20)
result2 = divide(30, 40)
result3 = minus(result1, result2)
print("1=>",result3)

print("2=>",minus(multiple(10, 20), divide(30, 40)))