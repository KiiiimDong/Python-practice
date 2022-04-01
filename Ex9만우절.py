#만우절제목추출
import requests
from bs4 import BeautifulSoup
url = 'https://search.naver.com/search.naver?query=%EB%A7%8C%EC%9A%B0%EC%A0%88&ie=utf8&sm=whl_nht'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
data=soup.select("a.api_txt_lines.total_tit_cross_trigger")
for i in data:
    t=i.get_text()
    print(t)