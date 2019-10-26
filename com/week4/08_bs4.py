from bs4 import BeautifulSoup

aaa = "<p><div>hello</div></p>"

bsObj = BeautifulSoup(aaa, "html.parser")
print(bsObj)
print(bsObj.find("div"))
