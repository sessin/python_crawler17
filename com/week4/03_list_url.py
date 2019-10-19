
# 028300, 000660, 078130
code = "000660"
# 문자열에서 1개만 골라내는 연산
# 문자열에서 맨뒤에 값을 추가(바꿔)하는 연산

# https://finance.naver.com/item/main.nhn?code=000660
# https://finance.naver.com/item/main.nhn?code=028300
# https://finance.naver.com/item/main.nhn?code=078130

codes = ["000660", "028300", "078130"]
# code를 넣으면 url을 return하는 함수를 만들어 보세요
def makeUrl(code):
    return "https://finance.naver.com/item/main.nhn?code={}".format(code)

for code in codes:
    print(makeUrl(code))


