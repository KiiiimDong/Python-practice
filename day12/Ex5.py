
import requests
from bs4 import BeautifulSoup
url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
r=requests.get(url)#html 가지고오기.
soup=BeautifulSoup(r.text,"html.parser")#정리
'abcda'
"""
t1=soup.find("a") # <a> </a>
print(t1)
print(type(t1))
l_t1=list(t1)
print(len(l_t1))
for i in t1:
    print(i)

print("-"*20)

t2=soup.find("div") # <a> </a>
print(t2)
print(type(t2))
l_t2=list(t2)
print(len(l_t2))
for i in t2:
    print(i)

print(t1.get_text())#t1=soup.a
"""
t2=soup.find("div")
print(t2.get_text())
print("-"*20)
t2=t2.next_sibling.next_sibling
print("-"*20)
#print(t2)
#print(type(t2))
#print(t2.a.get_text())
t3=soup.find_all("div")
sub_t3=list(t3)[:2]
for i in sub_t3:
    print(i.get_text())
    print("-"*20)

#print(t3)
#l_t3=list(t3)
#print(len(l_t3))
#print(l_t3[0])
#print(type(l_t3[0]))
#print(l_t3[0].a.get_text())
#for i in t3:
    #print(i.a.get_text())
