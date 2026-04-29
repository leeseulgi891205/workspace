import time
import os
import random

# 웹스크래핑
import requests
from bs4 import BeautifulSoup

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 이메일발송라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

#날짜함수
from datetime import datetime

# 마우스 제어
import pyautogui

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")

## selenium 함수
url = "https://www.daum.net/"
browser = webdriver.Chrome(options=options) # 창열기
browser.maximize_window() # 최대창 확대

# 1. daum 페이지 열기
browser.get(url)
time.sleep(2)

# 2. 검색창 찾기 및 검색어 입력
search_box = browser.find_element(By.CSS_SELECTOR, "#q")
search_box.click()
search_box.send_keys("서울특별시 용산구 한남동 아파트")
time.sleep(1)

# 3. 검색 버튼 클릭
search_button = browser.find_element(By.CSS_SELECTOR, ".btn_ksearch")
search_button.click()
time.sleep(3)

print("검색 완료!")

input("대기중. . . .")