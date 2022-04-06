import warnings
import time
warnings.filterwarnings('ignore') #warning 비활성화
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
b=webdriver.Chrome() #컨트롤러 실행
b.implicitly_wait(10) #활성화 될때까지 대기
b.get("http://naver.com")#요청(페이지 이동)
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click()
b.implicitly_wait(10)
b.find_element_by_xpath('/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[6]/a/span').click()
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="snb"]/ul/li[4]/a').click()
b.implicitly_wait(10)
html=b.page_source
for i in range(1, 6):
    print(f"{i}페이지")
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'//*[@id="main_content"]/div[3]/a[{i}]').click()
    b.implicitly_wait(10)
    s=BeautifulSoup(html,'html.parser')
    data=s.select('dl')
    for i in data:
        if i.a:
            print(i.dd.previous_sibling.previous_sibling.a.text.strip())
            print(i.dd.span.text.strip())
    print("출력완료")