import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
res = requests.get(url)
res.raise_for_status()


# 파일 저장방법  w저장 , r읽기, a추가
#f = open("aaa.html","w",encoding="utf8")
#f.write(res.text)
#f.close()

soup = BeautifulSoup(res.text, "lxml")

# soupo.prettify() : html 문서를 예쁘게 정렬
with open("aaa2.html","w",encoding="utf8") as f:
    f.write(soup.prettify())  #html 문서를 예쁘게 정렬해서 저장

print("파일이 저장되었습니다")