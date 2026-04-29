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
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C+%EC%9A%A9%EC%82%B0%EA%B5%AC+%ED%95%9C%EB%82%A8%EB%8F%99+%EC%95%84%ED%8C%8C%ED%8A%B8"
browser = webdriver.Chrome(options=options) # 창열기
browser.maximize_window() # 최대창 확대
browser.get(url)
time.sleep(2)


input("대기중. . . .")