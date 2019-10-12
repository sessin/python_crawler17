# crawl()
# parse()

# 028300 에이치엘비, 000660 SK하이닉스 두 회사의
# 가격과 코스닥인지 코스피인지 여부를 수집하는
# 크롤러(crawl + parse)를 만들고 데이터를 출력 해보세요
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    pNoToday = bsObj.find("p", {"class":"no_today"})
    blind = pNoToday.find("span", {"class":"blind"})
    price = blind.text
    description = bsObj.find("div", {"class":"description"})
    img = description.find("img")
    category = img['alt']

    return {"price":price, "category":category}

codes = ["028300", "000660"]
for code in codes:
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    print(companyInfo)

