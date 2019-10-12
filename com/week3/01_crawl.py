# 네이버 금융 특정 종목 가격, 회사이름을 크롤하고 파싱 해보세요

# crawl()
# url을 받아서 pageString을 return하는 함수를 만들어 보세요

import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    # print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    description = bsObj.find("div", {"class":"description"})
    img = description.find("img")
    print(img)

url = "https://finance.naver.com/item/main.nhn?code=028300"
pageString = crawl(url)
companyInfo = parse(pageString)


