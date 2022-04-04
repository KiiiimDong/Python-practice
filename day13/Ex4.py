from random import randint
import time
import csv
import requests #수집
from bs4 import BeautifulSoup #정리
url = "https://movie.naver.com/movie/point/af/list.naver?&page="#파일이름
title = "영화명","평점","리뷰"
f=open("save2.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
in_data=[]
#data 수집
for page in range(1,6):
    print(f"page{page} 크롤링중")
    #1개의 page를 로드(스크래핑)
    r=requests.get(url+str(page))
    r.raise_for_status() #접속 상태 확인 (접속 코드 200 아닐시 예외 발생)
    soup = BeautifulSoup(r.text,"html.parser")
    data = soup.find_all("td",attrs={"class":"title"})
    #파일정리
    for i in data:
        if i.a:
            in_data.append([i.a.text,i.em.text,i.br.next_sibling.strip()])
            # 단일입력
            # in_data=[i.a.text,i.em.text,i.br.next_sibling.strip()]
            # writer.writerow(in_data)
    time.sleep(randint(5,10))#빼먹으면 큰일난다.3초이상은 줘야한다.
#저장
writer.writerows(in_data)
