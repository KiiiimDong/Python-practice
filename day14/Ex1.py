"""
import requests
from bs4 import BeautifulSoup
url="data의 실질적인장소(html,css,javascript)"
r=requests.get(url)
"""
import requests
from bs4 import BeautifulSoup
url="data의주소"
r= requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
s.previous_sibling#next_sibling반대
