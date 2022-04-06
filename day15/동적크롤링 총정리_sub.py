import requests
from bs4 import BeautifulSoup
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
         "Accept-Language":"ko-KR,ko"}
r=requests.get('https://play.google.com/store/movies',headers=headers)
s=BeautifulSoup(r.text,'html.parser')
data=s.select('div.Epkrse')
for i in data:
    print(i.text)