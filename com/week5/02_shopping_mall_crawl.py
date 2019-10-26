import requests
from bs4 import BeautifulSoup

def crawl(url):
    res = requests.get(url)
    print(res)
    return res.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    info = bsObj.find("div", {"class":"info"})
    aTag = info.find("a")
    print(aTag.text)

url = "https://search.shopping.naver.com/search/all.nhn?query=%EC%B2%AD%EB%B0%94%EC%A7%80&cat_id=&frm=NVSHATC"
pageString = crawl(url)
products = parse(pageString)
