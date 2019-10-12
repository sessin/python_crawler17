# crawler, crawling - 데이터 받아오기
# 웹브라우저 crawl -> 렌더링
# 파이썬크롤러 -> crawl -> parse

# crawl함수를 만들고 데이터를 출력해보세요

import requests # crawl 하는 library
from bs4 import BeautifulSoup # parse 하는 library

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    wrap_company = bsObj.find("div", {"class":"wrap_company"})
    aTag = wrap_company.find("a")
    return {"price":blind.text, "name":aTag.text}

url = "https://finance.naver.com/item/main.nhn?code=028300"
pageString = crawl(url)
price = parse(pageString)
print(price)
print(price['price'], price['name'])


