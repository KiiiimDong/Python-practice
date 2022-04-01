import requests
from bs4 import BeautifulSoup
url = 'https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EC%9B%94%EB%93%9C%EC%BB%B5'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
data=soup.select("a.news_tit")
for i in data:
    t=i.get_text()
    print(t)
