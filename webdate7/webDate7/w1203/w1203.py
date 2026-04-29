import requests
from bs4 import BeautifulSoup
from selenuum import webdribver
import time

browser = webdriver.Chrome()
url = "http//www.naver.com"
headers = {"User-Agent": ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36""}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
print(soup.prettify())


