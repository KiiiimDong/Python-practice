from selenium import webdriver
from bs4 import BeautifulSoup
op = webdriver.ChromeOptions()
op.headless = True
op.add_argument("window-size=1920x1080")
op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
b = webdriver.Chrome(options=op)
b.maximize_window()
b.get("https://www.google.com/search?q=%EC%95%94%ED%98%B8%ED%99%94%ED%8F%90&oq=%EC%95%94%ED%98%B8%ED%99%94%ED%8F%90&aqs=chrome..69i57j0i512l6j69i60.1628j0j7&sourceid=chrome&ie=UTF-8")
s=BeautifulSoup(b.page_source,'html.parser')
b.quit()