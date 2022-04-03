import requests
from bs4 import BeautifulSoup
url = 'https://movie.naver.com/movie/point/af/list.naver'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
#1번
#data=soup.find("td",attrs={"class":"title"})
#print(data)

"""
data=soup.find_all("td",attrs={"class":"title"})
for i in data:
    print(i.a.get_text())
#print(data.a.get_text())
"""

#2번

#print(soup.select('td[class=title]'))
for i in soup.select('td[class=title]'):
    print(i.a.text.strip())