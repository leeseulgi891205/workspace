import requests
from bs4 import BeautifulSoup
import csv

# 웹페이지 주소와 요청 헤더 준비
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

# 웹페이지 요청해서 html 가져오기
res = requests.get(url, headers=headers)
res.raise_for_status()   # 문제가 있으면 에러 발생

# html을 BeautifulSoup으로 파싱하기
soup = BeautifulSoup(res.text, "lxml")

# 검색종목 테이블에서 모든 tr(행) 가져오기
trs = soup.find("div", {"class": "box_type_l"}).table.find_all("tr")

# 출력할 컬럼 이름(헤더)
header = ["순위","종목명","검색비율","현재가","전일비","등락률",
          "거래량","시가","고가","저가","PER","ROE"]

# 터미널에서 헤더 먼저 출력
print("\t".join(header))

# csv에 저장할 데이터를 담을 리스트
rows = []

# tr(행) 하나씩 반복하면서 데이터 추출하기
for tr in trs:
    tds = tr.find_all("td")

    # td가 12개 미만이면 데이터가 없는 빈 줄이므로 넘어가기
    if len(tds) < 12:
        continue

    # 순위가 숫자인지 확인
    rank_text = tds[0].get_text(strip=True)
    if not rank_text.isdigit():
        continue

    # 순위를 정수로 변환
    rank = int(rank_text)

    # 순위
    if rank > 30:
        continue

    # 각 컬럼 데이터 가져오기
    name = tds[1].get_text(strip=True)
    search_rate = tds[2].get_text(strip=True)
    price = tds[3].get_text(strip=True)
    diff = tds[4].get_text(strip=True)
    change_rate = tds[5].get_text(strip=True)
    volume = tds[6].get_text(strip=True)
    open_price = tds[7].get_text(strip=True)
    high = tds[8].get_text(strip=True)
    low = tds[9].get_text(strip=True)
    per = tds[10].get_text(strip=True)
    roe = tds[11].get_text(strip=True)

    # 한 줄(row) 데이터 만들기
    row = [rank,name,search_rate,price,diff,change_rate,
           volume,open_price,high,low,per,roe]

    # csv에 저장할 리스트에 추가
    rows.append(row)

    # 터미널에 출력
    print("\t".join(map(str, row)))

# 현재가가 가장 높은 주식 찾기
max_price = -1
max_row = None

for row in rows:
    price_str = str(row[3]).replace(",", "")
    if not price_str.isdigit():
        continue
    price_value = int(price_str)
    if price_value > max_price:
        max_price = price_value
        max_row = row

if max_row is not None:
    print("\n가장 비싼 주식:")
    print("\t".join(map(str, max_row)))

# csv 파일 이름 설정
file_name = "주식.csv"

# csv 파일로 저장하기
with open(file_name, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(header)   # 첫 줄: 컬럼명
    writer.writerows(rows)    # 다음 줄들: 데이터

# 저장 완료 메시지 출력
print(f"\ncsv 저장됨 → {file_name}")
f.close()
