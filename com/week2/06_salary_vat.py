# getSalary 연차 * 8000000 함수를 만들고
# 여러분들의 연봉을 구해보시기 바랍니다.
# getVAT(x) = x * 0.1

def getSalary(year):
    return year * 8000000

def getVAT(money):
    return money * 0.1

result = getSalary(7)
vat = getVAT(result)
print(result, vat)
print(vat)