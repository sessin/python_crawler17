# naver finance 회사이름, 가격, code, 코스닥인지 코스피인지
import requests
from bs4 import BeautifulSoup

# crawl
def crawl(url):
    res = requests.get(url)
    print(res)
    return res.content

# parse
def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    wrap_company = bsObj.find("div", {"class":"wrap_company"})
    code = wrap_company.find("span", {"class":"code"})
    aTag = wrap_company.find("a")
    img = wrap_company.find("img")
    pTag = bsObj.find("p", {"class":"no_today"})
    blind = pTag.find("span", {"class":"blind"})
    return {"name":aTag.text, "code":code.text, "category":img['alt'],
            "price":blind.text}

# ap:Kkomtle_Lounge5G pw: 20160919
companyInfos = []
codes = ["033180", "000660", "215600", "336370", "084990"]
for code in codes:
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyinfo = parse(pageString)
    companyInfos.append(companyinfo)
    print(companyinfo)
import json
print(json.dumps(companyInfos))