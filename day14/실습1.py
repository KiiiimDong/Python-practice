# https://land.naver.com/news/region.naver?&page= 뉴스 5페이지
# 개인에게 맞는 User-Agent 정보를 찾아서 헤더를 이용하여 접속.
# csv파일로 저장.
# 뉴스의 제목,내용 2가지를 이용하여 입력.
# 저장된 csv파일을 이용하여 내용 출력.
# randint sleep(3~6)
from random import randint
import time
import csv
import requests
from bs4 import BeautifulSoup
url = "https://land.naver.com/news/region.naver?&page="
title = "제목","내용"
f=open("save5.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
data_list=[]
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
#크롤링
for page in range(1,6):
    print(f"page{page} 크롤링중")
    r=requests.get(url+str(page),headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,"html.parser")
    data = soup.select("dl")

    for i in data:
        if i.a:#이거왜하는거임?
            data_list.append([i.dd.previous_sibling.previous_sibling.a.text.strip(),
                            i.dd.text.strip().replace(i.dd.span.text+"\n"+i.dd.span.next_sibling.next_sibling.text,"")])
    time.sleep(randint(3,6))#빼먹으면 큰일난다
#5.저장
writer.writerows(data_list)#2차원데이터 입력
f.close()
#6.로드 후 출력
f=open("save5.csv","r",encoding='utf-8-sig',newline="")
reader=csv.reader(f)
n=True
for i in reader:
    if n:#data전처리.
        n=False
        continue
    print(i[0],i[1])