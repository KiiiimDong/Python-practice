import time
import csv
import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=228&sid1=105&mid=shm&date=20220404&page="
title = "제목","축약내용"
f=open("save4.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
data_list=[]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
#data 수집
for page in range(1,6):
    print(f"page{page} 크롤링중")
    r=requests.get(url+str(page),headers=headers)
    r.raise_for_status() #r.text=html.
    soup = BeautifulSoup(r.text,"html.parser")
    data = soup.select("dl")
for i in data:
    if i.a:
        print(i.dd.previous_sibling.previous_sibling.a.text.strip())
        print(i.dd.span.text.strip())
f = open("save4.csv","r",encoding='utf-8-sig',newline="")
reader=csv.reader(f)
for i in reader:
    print(i)
