import requests#review꺼내오기.
from bs4 import BeautifulSoup
url = 'https://movie.naver.com/movie/point/af/list.naver'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
data=soup.select("td.title")

#1번
"""
for i in data:
    print(i.br.next_sibling.text.strip())
"""

#2번 데이터 특성을 이용한 코드
"""
for i in data:
    l=list(i)
    print(l[6].strip())
    """

#2번 확인하는방법
"""
l=[i for i in data]
a=[i for i in l[0]]
print(a[6].strip())
"""
