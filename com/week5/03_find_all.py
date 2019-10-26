from bs4 import BeautifulSoup

pageString = """
<html>
    <ul>
        <li>
            <div class='info'>
                <a>가을 신상 남자 청바지 ~~</a>
            </div>
        </li>
        <li>
            <div class='info'>
                <a>위드진 남자 청바지 ~~</a>
            </div>
        </li>
    </ul>
</html>
"""
def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    info = bsObj.find("div", {"class":"info"})
    aTag = info.find("a")
    print(aTag.text)

# 상품명만 뽑아보세요
parse(pageString)