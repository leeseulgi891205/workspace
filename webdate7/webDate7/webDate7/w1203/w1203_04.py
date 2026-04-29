import requests  # (사용 안함) 원래는 웹사이트 요청할 때 쓰는 라이브러리
from bs4 import BeautifulSoup # HTML을 예쁘게 뜯어주는 라이브러리
from selenium import webdriver
import time
import os
import csv

# 3. 저장해둔 gmarket1.html 파일을 불러와서 분석하기
with open("gmarket1.html","r",encoding="utf8") as f:
    # HTML 파일 내용을 BeautifulSoup으로 파싱(해석)하기
    soup = BeautifulSoup(f,"lxml")

# ul 태그 중 class가 list__best 인 것을 찾기 (상품 리스트 전체)
ul = soup.find("ul",{"class":"list__best"})

# 최고 가격을 저장할 변수 (0으로 시작)
max_price = 0  

# ul 안에 있는 모든 li 태그(상품 하나하나)를 찾기
lis = ul.find_all("li")

# CSV 파일(gmarket.csv)을 새로 열고, 쓰기 모드로 준비
f = open("gmarket.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

# CSV 파일의 첫 줄(컬럼 이름) 적기
writer.writerow(['순위','링크','제목','가격'])

# 상품 10개를 출력하고 CSV에도 저장하기
for li in lis:
    try:
        # 상품 순위 읽기
        rank = li.find("span",{"class":"box__label-rank"}).text.strip()

        # 이미지 링크(src) 가져오기 → 앞에 http: 붙여서 URL 만들기
        link = "http:"+li.find("img")['src']

        # 상품 제목 가져오기
        p_title = li.find("p",{"class":"box__item-title"}).text.strip()

        # 상품 가격 부분 전체 가져오기
        price_original = li.find("div",{"class":"box__price-seller"})

        # 가격 숫자만 뽑아서 int(정수)로 변환하기
        price = int(
            price_original.find("span",{"class":"text text__value"})
            .text.strip()
            .replace(",","")
        )

        # CSV 파일에 한 줄 추가하기
        writer.writerow([rank,link,p_title,price])

        # 터미널로도 출력하기
        print(rank)
        print(link)
        print(p_title)
        print(price)

        # 최고가일 경우 max_price 갱신하기
        if max_price < price:
            max_price = price

        print(price)
        print("-"*50)

    except:
        # 오류가 난 상품은 스킵
        print("[[[  예외 처리 ]]]")

# CSV 파일 닫기
f.close()

# 최고가격 출력
print("최고가격 : ", max_price)



###############################################
# 아래는 selenium으로 웹페이지 저장하는 코드.
# 지금은 주석 처리된 상태라 실행 안됨.
###############################################

# browser = webdriver.Chrome()
# browser.get("https://www.gmarket.co.kr/n/best?spm=gmktpc.home.0.0.1fbf486axva25P")
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")
# with open("gmarket1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("파일저장")
