import requests
from bs4 import BeautifulSoup

url="http://www.naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 파일저장
with open("naver_requests.html","w",encoding="utf8") as f:
    f.write(soup.prettify())