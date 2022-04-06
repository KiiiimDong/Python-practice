import time
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
b=webdriver.Chrome()
b.maximize_window()#크기결정.
b.implicitly_wait(10)
b.get("http://google.com")
b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("뉴스\n")
b.implicitly_wait(10)
b.execute_script("window.scrollTo(0,500)")
b.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div[1]/div/a/h3').click()
b.implicitly_wait(10)
#모든 내용을 담고있는 페이지 최하단.
while True:
    info_n = b.execute_script("return document.body.scrollHeight")
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#확장
    time.sleep(2)
    next_n=b.execute_script("return document.body.scrollHeight")
    if info_n==next_n:
        break
