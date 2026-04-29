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

#날짜함수
from datetime import datetime

### 임시비밀번호 생성함수
def random_pw():
    arr = [ i for i in range(10)]
    ranNum = "".join(map(str,random.sample(arr,8)))
    print("임시비밀번호 : "+ranNum)
    return ranNum
#------------------------------------------------------
# [ 웹스크래핑 정보 ]
#### selenium 방법
url = "http://www.naver.com"
browser = webdriver.Chrome() # 창열기
browser.get(url)
time.sleep(3)  # 페이지 완전히 로딩될 때까지 대기
soup = BeautifulSoup(browser.page_source,"lxml")
browser.quit()

# 파일로 저장하려면 아래 주석 해제
# with open('naver1.html','w',encoding="utf8") as f:
#     f.write(soup.prettify())

# 파일에서 읽으려면 아래 주석 해제
# with open('naver1.html','r',encoding='utf8') as f:
#     soup = BeautifulSoup(f,"lxml")
    
## 날짜
today = datetime.today()
now = today.strftime('%Y-%m-%d %H:%M:%S')
print(now)
## 온도/날씨
weather_div = soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"})
if weather_div:
    weather = weather_div.text.strip().replace(" ","").split("\n")
    weather = [w for w in weather if w]  # 빈 문자열 제거
    print("날씨 리스트:", weather)
    if len(weather) >= 2:
        today_weather = f"기온 : {weather[0]} / 날씨 : {weather[1]}"
    else:
        today_weather = f"기온 : {weather[0]}" if len(weather) > 0 else "날씨 정보 없음"
else:
    today_weather = "날씨 정보 없음"

low_temp_span = soup.find("span",{"class":"DailyBoardView-module__temperature_low___aC6Fe"})
if low_temp_span:
    low_temp = low_temp_span.text.strip().replace(" ","").split('\n')
    low_temp = [l for l in low_temp if l]  # 빈 문자열 제거
    print("최저기온 리스트:", low_temp)
    if len(low_temp) >= 2:
        today_low_temp = f"{low_temp[0]} : {low_temp[1]}"
    else:
        today_low_temp = f"{low_temp[0]}" if len(low_temp) > 0 else "최저기온 정보 없음"
else:
    today_low_temp = "최저기온 정보 없음"

content = f'''{now}
{today_weather}
{today_low_temp}'''
print(content)

# 2. 엔비디아 주식 정보 스크래핑
print("\n엔비디아 주식 정보 가져오는 중...")
browser2 = webdriver.Chrome()
# 네이버 검색 - 엔비디아
nvidia_url = "https://search.naver.com/search.naver?where=nexearch&query=엔비디아"
browser2.get(nvidia_url)
time.sleep(3)
stock_soup = BeautifulSoup(browser2.page_source, "lxml")

# 현재가
current_price_elem = stock_soup.find("strong", {"class": "spot_price"})
if not current_price_elem:
    current_price_elem = stock_soup.find("span", {"class": "spt_con"})
if not current_price_elem:
    current_price_elem = stock_soup.find("em", {"class": "spt_con"})
if current_price_elem:
    price_text = current_price_elem.get_text().strip()
else:
    price_text = "가격 정보 없음"

# 전일대비 - 상승/하락 금액
change_elem = stock_soup.find("em", {"class": "spt_con2"})
if not change_elem:
    change_elem = stock_soup.find("span", {"class": "gap"})
if change_elem:
    change_text = change_elem.get_text().strip()
else:
    change_text = "변동 정보 없음"

# 등락률
rate_elem = stock_soup.find("span", {"class": "rate"})
if not rate_elem:
    rate_elem = stock_soup.find("em", {"class": "spt_con3"})
if rate_elem:
    rate_text = rate_elem.get_text().strip()
else:
    rate_text = ""

browser2.quit()

stock_info = f'''

[엔비디아(NVDA) 주식 정보]
현재가: {price_text}
전일대비: {change_text} {rate_text}
'''

print(stock_info)

# 3. 삼성전자 주식 정보 스크래핑
print("\n삼성전자 주식 정보 가져오는 중...")
browser3 = webdriver.Chrome()
# 네이버 검색 - 삼성전자
samsung_url = "https://search.naver.com/search.naver?where=nexearch&query=삼성전자"
browser3.get(samsung_url)
time.sleep(3)
samsung_soup = BeautifulSoup(browser3.page_source, "lxml")

# 현재가
samsung_price_elem = samsung_soup.find("strong", {"class": "spot_price"})
if not samsung_price_elem:
    samsung_price_elem = samsung_soup.find("span", {"class": "spt_con"})
if not samsung_price_elem:
    samsung_price_elem = samsung_soup.find("em", {"class": "spt_con"})
if samsung_price_elem:
    samsung_price_text = samsung_price_elem.get_text().strip()
else:
    samsung_price_text = "가격 정보 없음"

# 전일대비
samsung_change_elem = samsung_soup.find("em", {"class": "spt_con2"})
if not samsung_change_elem:
    samsung_change_elem = samsung_soup.find("span", {"class": "gap"})
if samsung_change_elem:
    samsung_change_text = samsung_change_elem.get_text().strip()
else:
    samsung_change_text = "변동 정보 없음"

# 등락률
samsung_rate_elem = samsung_soup.find("span", {"class": "rate"})
if not samsung_rate_elem:
    samsung_rate_elem = samsung_soup.find("em", {"class": "spt_con3"})
if samsung_rate_elem:
    samsung_rate_text = samsung_rate_elem.get_text().strip()
else:
    samsung_rate_text = ""

browser3.quit()

samsung_info = f'''
[삼성전자 주식 정보]
현재가: {samsung_price_text}
전일대비: {samsung_change_text} {samsung_rate_text}
'''

print(samsung_info)

# 날씨 정보와 주식 정보 합치기
content = f'''{now}
{today_weather}
{today_low_temp}
{stock_info}
{samsung_info}'''




# [ 웹스크래핑 정보 끝 ]
#-----------------------------------------------
# content = f'''
# 임시비밀번호 : {random_pw()}
# '''
# 메일내용부분

msg = MIMEText(content)
msg['From'] = "crsm5207@naver.com" #보내는이 - 네이버 보내는 주소 naver.com
msg['To'] = "crsm5207@naver.com"   #받는이 - onulee74@gmail.com
msg['Subject'] = "이슬기 이메일 보내드립니다."
# 메일서버 정보
s = smtplib.SMTP("smtp.naver.com",587)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("crsm5207@naver.com","4EKV6WD5NVTJ")
# 메일서버 발송 - 보내는이메일주소,받는주소,이메일내용부분
s.sendmail("crsm5207@naver.com","onulee@naver.com",msg.as_string())
# 메일 닫기
s.close()
print("이메일 발송완료")