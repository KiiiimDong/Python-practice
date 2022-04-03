#도서명에대해서만 받아보기.
import requests
from bs4 import BeautifulSoup
url = 'https://www.hanbit.co.kr/store/books/full_book_list.html'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
for i in soup.select('td[class=left]'):
    if i.a:
        print(i.a.text)
for i in soup.find_all("td",attrs={"class":"title"}):
    print(i)
#href="/store/books/look.php?p_code
