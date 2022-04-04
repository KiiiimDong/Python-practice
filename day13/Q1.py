import requests
from bs4 import BeautifulSoup
import sqlite3
url = "https://finance.naver.com/sise/sise_quant.naver?sosok=1"
r=requests.get(url)
html_d=r.text
soup=BeautifulSoup(html_d,'html.parser')
data=soup.select("td")
def f(n,x):
    for i in range(x):
         n=n.next_sibling
    return n.text.strip()
for i in data:
    if i.a:
        in_data = f"[종목명:{i.a.text}],[현재가:{f(i,2)}],[전일비:{f(i,4)}],[등락률:{f(i,6)}],[거래량:{f(i,8)}],[거래대금:{f(i,10)}],[매수호가:{f(i,12)}],[매도호가:{f(i,14)}],[시가총액:{f(i,16)}],[PER:{f(i,18)}],[ROE:{f(i,20)}]"

db="in_data.db"
def 저장(db,in_data):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS in_data')
    c.execute('''
                CREATE TABLE data(
                    종목명 text,
                    현재가 text,
                    전일비 text,
                    등락률 text,
                    거래량 text,
                    거래대금 text,
                    매수호가 text,
                    매도호가 text,
                    시가총액 text,
                    PER text,
                    ROE text
                )
            ''')
    c.executemany('INSERT INTO data VALUES(:종목명,:현재가,:전일비,:등락률,:거래량,:거래대금,:매수호가,:매도호가,:시가총액,:PER,:ROE)',in_data)
    conn.commit()
    conn.close()

def 출력(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(i)
#저장(db,in_data)
#출력(db)
print(in_data)
