import requests
from bs4 import BeautifulSoup
url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
import requests
r=requests.get(url)
#print(r.text)
soup=BeautifulSoup(r.text,"lxml")#lxml,html.parser
#print(soup)
#print(soup.title.get_text())
#print(soup.a.attrs)
#print(soup.a['href'])
#print(soup.find('a',attrs={"href":"/store/books/look.php?p_code=B9483006177"}).get_text())
#print(soup.find('a',attrs={"href":"/store/books/look.php?p_code=B5744853316"}).get_text())
#print(soup.find(attrs={"href":"/store/books/look.php?p_code=B5744853316"}))
k=print(soup.find('div',attrs={'class':"full_book_list_wrap"}))

print(type(soup))
print(type(k))
