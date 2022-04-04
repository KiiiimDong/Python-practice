import requests #수집
from bs4 import BeautifulSoup #정리
url = "https://movie.naver.com/movie/point/af/list.naver?&page="#파일이름
page=10
r=requests.get(url+str(page))
r.raise_for_status() #접속 상태 확인 (접속 코드 200 아닐시 예외 발생)
soup = BeautifulSoup(r.text,"html.parser")
data = soup.find_all("td",attrs={"class":"title"})
#data.find("a").text
data_l=[]
for i in data:
    if i.a:
        data_l.append({"영화명":i.a.text,
        "평점":i.em.text,
        "리뷰":i.br.next_sibling.strip()})
import sqlite3
conn=sqlite3.connect("data_ex3.db")
c=conn.cursor()
c.execute('DROP TABLE IF EXISTS data')
c.execute('''
            CREATE TABLE data (
            영화명 text,
            평점 text,
            리뷰 text
            )
        ''')
c.executemany('INSERT INTO data VALUES (:영화명,:평점,:리뷰)',data_l)
conn.commit()
conn.close()
def 출력():
    conn = sqlite3.connect("data_ex3.db")
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(f"영화명 {i[0]},평점 {i[1]} ,리뷰 {i[2]}")
