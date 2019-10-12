# 파이썬 웹 데이터 수집
# 크롤링, 스크래핑, 파싱
# 크롤링 - 데이터 수집
# 파싱 - 데이터에서 정보를 뽑아내는 것
# 스크래핑 - 크롤링 + 파싱
# 크롤러(crawler) + 파서(parser)

# 라이브러리 library 모듈 module
import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    print(bsObj)

url = "https://finance.naver.com/item/main.nhn?code=028300"
pageString = crawl(url)
print(pageString)
compantInfo = parse(pageString)