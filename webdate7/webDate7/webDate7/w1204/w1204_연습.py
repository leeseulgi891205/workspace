from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import time
import os
import random

url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window() # 최대화면
# 1. naver 페이지 열기
browser.get(url)

popup_selectors = [
    "//button[contains(text(), '닫기')]",
    "//button[contains(text(), 'Close')]",
    "//button[@aria-label='닫기']",
    "//button[contains(@class, 'close')]",
    "//button[contains(@class, 'btn_close')]",
    "//div[contains(@class, 'layer')]//button",
]

for selector in popup_selectors:
    try:
        btn = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
        btn.click()
        print("팝업 닫힘:", selector)
        break
    except:
        pass
    
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/i').click()
# 김포 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()
# 제주선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()
# 가는날 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
# 가는날 26일 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[5]/td[2]/button/b').click()
# 오는날 27일 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[5]/td[3]/button/b').click()
# 검색버튼
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/button').click()

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