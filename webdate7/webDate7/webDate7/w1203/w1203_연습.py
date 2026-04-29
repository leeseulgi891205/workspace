from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import re

# 1. 크롬 드라이버 실행
service = Service()
driver = webdriver.Chrome(service=service)

url = "https://www.gmarket.co.kr/n/best?spm=gmktpc.home.0.0.275b486aTEe4xZ"
driver.get(url)

# 2. 페이지 로딩 대기
time.sleep(3)

# 3. HTML 파싱
soup = BeautifulSoup(driver.page_source, "lxml")
items = soup.select("div.box__best-list ul.list__best li.list-item")

max_price_value = -1
max_price_item = None  

output = []  # 파일 저장용 리스트

output.append("===== 상품 =====\n")
print("===== 상품 =====")

for idx, item in enumerate(items, start=1):
    title_tag = item.select_one(".box__item-title")
    if not title_tag:
        continue

    title = title_tag.get_text(strip=True)

    # 이미지
    img_tag = item.select_one(".box__thumbnail img.image")
    img = img_tag["src"] if img_tag else "이미지 없음"

    # 가격
    price_tag = item.select_one(".box__item-price")
    price_text = price_tag.get_text(strip=True) if price_tag else "가격 없음"

    # 숫자만 추출해 비교가격 만들기
    numbers = re.findall(r"\d+", price_text)
    price_value = int("".join(numbers)) if numbers else 0

    # 출력 + 저장
    if idx <= 200:
        line = (
            f"번호: {idx}\n"
            f"이미지: {img}\n"
            f"제목: {title}\n"
            f"가격: {price_text}\n"
            + "-" * 40 + "\n"
        )
        print(line, end="")
        output.append(line)

    # 최고가 갱신
    if price_value > max_price_value:
        max_price_value = price_value
        max_price_item = (img, title, price_text)

driver.quit()

# 4. 최고가 출력 & 저장
output.append("\n===== 최고가 상품 =====\n")
print("\n===== 최고가 상품 =====")

if max_price_item:
    line = (
        f"이미지: {max_price_item[0]}\n"
        f"제목: {max_price_item[1]}\n"
        f"가격: {max_price_item[2]}\n"
        
    )
    print(line)
    output.append(line)
else:
    print("상품 없음")
    output.append("상품 없음\n")

# 5. 파일 저장
with open("gmarket.csv", "w", encoding="utf-8") as f:
    f.writelines(output)
f.close()

print("파일이 저장되었습니다.")