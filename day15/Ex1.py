import warnings
warnings.filterwarnings('ignore') #warning 비활성화
import time #sleep 쓰기위해서
#접근방식
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
b=webdriver.Chrome() #컨트롤러 실행
b.implicitly_wait(10) #활성화 될때까지 대기
#time.sleep(초단위)#스레드를 정지.
b.get("http://naver.com")#요청(페이지 이동)
#c=webdriver.Chrome()
#c.get("https://www.daum.net") #단일로 쓰는것 권장.
in_t=b.find_element_by_xpath('//*[@id="query"]')#위치찾기
in_t.send_keys("뉴스") #키보드입력
b.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
b.implicitly_wait(10) #활성화 될때까지 대기
#b.find_element_by_xpath('//@[id="lnb"]/div[1]/div/ul~~~')