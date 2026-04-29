import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# requests라이브러리, selenium라이브러리 차이점.
# 크롬드라이버를 활용해서 크롬브라우저를 제어할수 있음.
browser = webdriver.Chrome()
# 크롬브라우저 창이 열림.
browser.get("https://comic.naver.com/index")

time.sleep(7) # 3초 대기후 실행
soup = BeautifulSoup(browser.page_source,"lxml")
# 파일저장
with open("webtoon_browser.html","w",encoding="utf8") as f:
    f.write(soup.prettify())





# url="https://www.daum.net/"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# print(res.text)