companies = [
    {'name': '필룩스', 'code': '033180', 'category': '코스피', 'price': 6590},
    {'name': 'SK하이닉스', 'code': '000660', 'category': '코스피', 'price': 77400},
    {'name': '신라젠', 'code': '215600', 'category': '코스닥', 'price': 12750},
    {'name': '두산솔루스', 'code': '336370', 'category': '코스피', 'price': 5510},
    {'name': '헬릭스미스', 'code': '084990', 'category': '코스닥', 'price': 84300},
    {'name': '삼성전자', 'code': '005930', 'category': '코스피', 'price': 49900},
    {'name': '셀트리온', 'code': '068270', 'category': '코스피', 'price': 181500},

    {'name': 'KT&G', 'code': '033780', 'category': '코스피', 'price': 103000},
    {'name': '우진비앤지', 'code': '018620', 'category': '코스닥', 'price': 3190}
]

# 코스피가 많을까요 코스닥이 많을까요?
# category가 코스피인 회사 개수는 몇개일까요?

count = 0
for company in companies:
    if company["category"] == "코스피":
        count = count + 1
print(count)

# 한주당 평균 가격 구하는 function
def getAveragePrice(companies):
    sum = 0
    for company in companies:
        sum = sum + company['price']
    return sum / len(companies)

# sum구하는 함수를 만들어 보세요
# getPriceSum()

getPriceSum = lambda list:sum([item['price'] for item in list])

# csv -> comma separated value
# 필룩스,000123,코스피,15000
print("average:",getAveragePrice(companies))
print("sum:",getPriceSum(companies))