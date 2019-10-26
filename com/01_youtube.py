import requests
from bs4 import BeautifulSoup

def crawl(url):
    res = requests.get(url)
    # print(res)
    return res.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    divs = bsObj.findAll("div", {"class":"yt-lockup-content"})

    for div in divs:
        try:
            byline = div.find("div", {"class":"yt-lockup-byline"})
            byLineATag = byline.find("a")

            # print(sessionlink)
            aTag = div.find("a")
            ul = div.find("ul", {"class":"yt-lockup-meta-info"})
            metaInfoLis = ul.findAll("li")
            result = {"유투버":byLineATag.text, "제목":aTag.text, "조회수":metaInfoLis[1].text}
            print(result)
        except:
            print("error")



url = "https://www.youtube.com/results?search_query=발레"
pageString = crawl(url)
list = parse(pageString)
# print(pageString)