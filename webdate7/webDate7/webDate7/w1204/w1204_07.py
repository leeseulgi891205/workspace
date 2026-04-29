from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import os
import random

url = "https://flight.naver.com/"
browser = webdriver.Chrome() # 창열기
browser.maximize_window() # 최대창 확대
# 1. naver 페이지 열기
browser.get(url)
# 다른 탭 선택 - 네이버항공권 탭 선택됨.
# browser.switch_to.window(browser.window_handles[1])
# 광고알림창 닫기 버튼
elem = browser.find_element(By.XPATH,'//*[@id="layer"]/button[2]')
time.sleep(1)
elem.click()

# 1. 김포, 제주 선택
# 김포선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()

# 제주선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()

# 날짜선택 - # 달력열기
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
time.sleep(1)
elem.click()

# 가는날선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[2]/button')
time.sleep(1)
elem.click()

# 오는날선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[5]/td[3]/button')
time.sleep(1)
elem.click()

# 검색선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/button')
time.sleep(1)
elem.click()
input("대기")

# 4. 스크롤을 내려서 모든 항공사 정보 로딩
import time
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height
input("대기")