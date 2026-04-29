from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
import os
browser = webdriver.Chrome()
url = "http://www.naver.com"
# 1. 네이버 페이지 열기
browser.get(url)
# 2. 네이버 페이지에서 '시가총액' 입력
elem = browser.find_element(By.ID,"query")
elem.click()
elem.send_keys("시가총액 순위")
# 3. 엔터 입력
elem.send_keys(Keys.ENTER)
time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[2]/div/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')
elem.click()


input("대기")




#-----------------------------------------------------------------------------
# selenium 4.3버전에서 찾기 변경됨
#elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# 클릭 명령어
#elem.click()
# input 글자 입력
#elem.send_keys("시가총액")
# input 엔터 입력
#elem.send_keys(Keys.ENTER)
#input("대기")