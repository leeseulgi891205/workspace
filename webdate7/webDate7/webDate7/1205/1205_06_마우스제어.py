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

## selenium 함수
url = "https://www.naver.com/"
browser = webdriver.Chrome() # 창열기
browser.maximize_window() # 최대창 확대
# 1. naver 페이지 열기
browser.get(url)

pyautogui.sleep(1)
pyautogui.click(-700) 
pyautogui.scroll(700)
pyautogui.sleep(1)
pyautogui.moveTo(870,300)
pyautogui.click()
# pyautogui.doubleClick()
input("대기중. . . .") 
