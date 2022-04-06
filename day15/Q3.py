#기본셋팅
import warnings
warnings.filterwarnings('ignore')
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
#파일열기
title = "제목","내용"
f=open("save2.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
#data list
data_l=[]
data_l2=[]
#headless설정
op = webdriver.ChromeOptions()
op.headless = True
op.add_argument("window-size=1920x1080")
op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
b = webdriver.Chrome(options=op)
b.maximize_window()
#들어가는 과정
b.implicitly_wait(10)
b.get("https://www.google.co.kr/webhp?hl=ko&sa=X&ved=0ahUKEwipl4voyv72AhWPBN4KHR4YBDwQPAgI")
b.implicitly_wait(10)
b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("lck\n")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[4]/a').click()
b.implicitly_wait(10)
#for문으로 받아오기.
for i in range(3,8):
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    html=b.page_source
    b.find_element_by_xpath(f'//*[@id="xjs"]/table/tbody/tr/td[{i}]/a').click()
    b.implicitly_wait(10)
    s=BeautifulSoup(html,'html.parser')
    data1=s.find_all('div',attrs={"class":"mCBkyc y355M JQe2Ld nDgy9d"})
    data2=s.find_all('div',attrs={"class":"GI74Re nDgy9d"})
    for i in data1:
        data_l.append(i.text)
    for i in data2:
        data_l2.append(i.text)
    data_all=zip(data_l,data_l2)
#저장
writer.writerows(data_all)
f.close()
#로드 후 출력
f=open("save2.csv","r",encoding='utf-8-sig',newline="")
reader=csv.reader(f)
n=True
for i in reader:
    if n:
        n=False
        continue
    print(i[0],i[1])
b.quit()
