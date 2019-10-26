# 네이버 금융 특정 종목 데이터 수집하기
# crawl, parse만들고 회사 이름, 가격, 코스피인지 코스닥인지, 코드
import requests
from bs4 import BeautifulSoup

def crawl(url):
    res = requests.get(url)
    print(res)
    return res.content


def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    wrapCompany = bsObj.find("div", {"wrap_company"})
    aTag = wrapCompany.find("a")
    code = wrapCompany.find("span", {"class":"code"})
    img = wrapCompany.find("img")
    no_today = bsObj.find("p", {"class":"no_today"})
    blind = no_today.find("span", {"class":"blind"})
    return {"name":aTag.text, "code":code.text, "category":img['alt'],
            "price":blind.text}


def getCompanyInfo(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    return companyInfo

codes = ["028300", "000660"]
companyInfo = getCompanyInfo(codes[0])
print(companyInfo)
