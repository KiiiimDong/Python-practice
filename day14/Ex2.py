import time
from selenium import webdriver#웹 컨트롤러.
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
browser.get("http://www.google.com")
#browser.find_element_by_css_selector("input.gLFyf.gsfi").send_keys("python")
l=browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
l.send_keys("뉴스")
l.send_keys(Keys.RETURN)
browser.implicitly_wait(10)#창뜰때까지 기다리는거
#browser.execute_script("window.scrollTo(0,500);")#스크롤을 500만큼 내려라
ck=browser.find_element_by_xpath("//*[@id='rso']/div[2]/div/div/div[1]/div/a/h3")#xpath는 위치.
ck.click()
browser.implicitly_wait(10)
for i in range(5):
    browser.execute_script("window.scrollTo(0,500);")
    browser.implicitly_wait(10)

#이상한거
"""k=0
for i in range(1,10):
    g=k*i+100
    browser.execute_script(f"window.scrollTo({k},{g});")
    time.sleep(3)
    g=k"""