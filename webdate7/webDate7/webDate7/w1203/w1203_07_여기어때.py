from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import re  
import csv

# 크롬 옵션
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")

browser = uc.Chrome(options=options)
url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&personal=2&checkIn=2025-12-26&checkOut=2025-12-28&typoCorrect=true&nonAffiliated=true&sortType=RECOMMEND&category=2"
browser.get(url)

# 기본 로딩 대기
time.sleep(10)


last_height = browser.execute_script("return document.body.scrollHeight")

for _ in range(5):  # 필요하면 숫자 늘려도 됨
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 스크롤 후 로딩 대기
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 스크롤 끝난 뒤 HTML 가져오기
soup = BeautifulSoup(browser.page_source, "lxml")
items = soup.select("div.gc-thumbnail-type-seller-card-wrapper")

print("\n===== 숙소 리스트 =====\n")
print("총 개수:", len(items), "개\n")

rows = []

for idx, item in enumerate(items, start=1):
    # 숙소명
    name_tag = item.select_one("h3.gc-thumbnail-type-seller-card-title")
    name = name_tag.get_text(strip=True) if name_tag else "정보 없음"
    # 이미지 url (가능한 모든 경우 커버)
    img_tag = item.select_one("img")
    image_url = None
    if img_tag:
        if img_tag.get("src"):
            image_url = img_tag.get("src")
        elif img_tag.get("data-src"):
            image_url = img_tag.get("data-src")
        elif img_tag.get("srcset"):
            image_url = img_tag.get("srcset").split(" ")[0]
    if not image_url:
        image_url = "정보 없음"
    # 위치
    city = item.select_one("span.css-1rzfout")
    city = city.get_text(strip=True) if city else "정보 없음"
    area = item.select_one("span.css-ki0lqh")
    area = area.get_text(strip=True) if area else "정보 없음"
    # 평점
    rating_tag = item.select_one("span.css-9ml4lz")
    rating = rating_tag.get_text(strip=True) if rating_tag else "정보 없음"
    # 리뷰수
    review_tag = item.select_one("span.css-oj6onp")
    reviews = review_tag.get_text(strip=True).replace("명 평가", "").strip() if review_tag else "정보 없음"
    # 정가 / 할인가 / 1박 가격
    full_price_tag = item.select_one("div.css-xgwoxj")
    full_price = full_price_tag.get_text(strip=True).replace("원", "") if full_price_tag else "정보 없음"
    sale_price_tag = item.select_one("span.css-5r5920")
    sale_price = sale_price_tag.get_text(strip=True) if sale_price_tag else "정보 없음"
    per_night_tag = item.select_one("span.css-fihc6t")
    per_night = per_night_tag.get_text(strip=True) if per_night_tag else ""

    # 터미널 출력
    print(f"[{idx}]")
    print("숙소명:", name)
    print("이미지 url:", image_url)
    print("위치:", city, "/", area)
    print("평점:", rating)
    print("리뷰수:", reviews)
    print("정가:", full_price)
    print("할인가:", sale_price)
    print("/1박:", per_night)
    print("-" * 50)

    rows.append([
        name,
        image_url,
        city,
        area,
        rating,
        reviews,
        full_price,
        sale_price,
        per_night,
    ])

browser.quit()

# csv 파일로 저장
filename = "여기어때.csv"
with open(filename, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["숙소명", "이미지url", "도시", "상세위치", "평점", "리뷰수", "정가", "할인가", "1박표시"])
    writer.writerows(rows)

print(f"\n csv 저장 완료: {filename}")
