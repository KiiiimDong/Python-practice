#1.네이버 뉴스 it 과학기사 수집(제목,축약내용)
#2.연속적 페이지 전환으로 수집. 단 sleep 5초.
#3..csv파일로 저장.
import time
import csv
import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=228&sid1=105&mid=shm&date=20220404&page="
title = "제목","축약내용"
f=open("save3.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
in_data=[]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
#data 수집
for page in range(1,6):
    print(f"page{page} 크롤링중")
    r=requests.get(url+str(page),headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,"html.parser")
    data = soup.select("dl")
    #파일정리
    for i in data:
        if i.a:
            in_data.append([i.a.text.strip(),i.span.text.strip()])
    time.sleep(6)#빼먹으면 큰일난다
writer.writerows(in_data)