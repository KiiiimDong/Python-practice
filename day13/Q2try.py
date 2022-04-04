import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=228&sid1=105&mid=shm&date=20220404&page=1"
title = "제목","축약내용"
in_data=[]
#data 수집
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
r=requests.get(url,headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.text,"html.parser")
data = soup.select("dl")
for i in data:
    if i.a:
        in_data.append([i.a.text.strip(),i.span.text.strip()])
print(in_data)

