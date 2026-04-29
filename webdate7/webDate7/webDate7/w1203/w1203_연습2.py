from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import re  # 리뷰수 숫자 추출용
import csv  # csv 저장용

# 크롬 옵션 설정
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")

# 크롬 실행
browser = uc.Chrome(options=options)

# 크롤링할 url
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&page=1"
browser.get(url)

# 페이지 로딩
time.sleep(5)

# html 가져와서 BeautifulSoup에 넣기
soup = BeautifulSoup(browser.page_source, "lxml")

# 상품명/가격/쿠폰 정보 뽑기
products = soup.find_all("div", {"class": "ProductUnit_productNameV2__cV9cw"})

print(f"상품 개수(이름 div 기준): {len(products)}개\n")

# csv 저장용 리스트
rows = []

for idx, name_div in enumerate(products, start=1):
    # 제품명 텍스트
    name = name_div.get_text(strip=True)
    price_area = name_div.find_next("div", {"class": "PriceArea_priceArea__NntJz"})

    # 쿠폰/가격 변수 초기화
    coupon_text = None
    original_price_int = None   # 정가 (할인 전 가격)
    sale_price_int = None       # 할인가 (실제 판매가)

    # 리뷰수 변수
    review_count = None

    # 실제 리뷰수: 상품명 이후에 나오는 리뷰 span을 범용적으로 탐색
    review_span = name_div.find_next(
        "span",
        {"class": lambda c: c and "RatingStar_totalCount" in c}
    )

    # 리뷰 span이 없으면 다음 span들을 탐색
    if not review_span:
        candidate_span = name_div.find_next("span")
        while candidate_span:
            txt = candidate_span.get_text(strip=True)
            if txt.startswith("(") and txt.endswith(")") and re.search(r"\d", txt):
                review_span = candidate_span
                break
            candidate_span = candidate_span.find_next("span")

    # 리뷰수 추출
    if review_span:
        txt = review_span.get_text(strip=True)
        txt = txt.replace("(", "").replace(")", "").replace(",", "")
        if txt.isdigit():
            review_count = int(txt)

    # 쿠폰/정가/할인가 추출
    if price_area:
        # 쿠폰 문구
        coupon_span = price_area.find("span", {"class": "fw-text-red-700"})
        if coupon_span:
            coupon_text = coupon_span.get_text(strip=True)

        # 정가: <del> 태그
        del_tag = price_area.find("del")
        if del_tag:
            original_price_str = del_tag.get_text(strip=True)
            original_price_int = int(
                original_price_str.replace(",", "").replace("원", "").strip()
            )

        # 할인가: 보통 <strong> 태그 안에 있음
        sale_tag = price_area.find("strong")
        if sale_tag:
            sale_price_str = sale_tag.get_text(strip=True)
            # 숫자만 뽑아서 정수로 변환
            sale_price_str = re.sub(r"[^0-9]", "", sale_price_str)
            if sale_price_str.isdigit():
                sale_price_int = int(sale_price_str)

    # 할인가가 없으면 다음 상품으로
    if sale_price_int is None:
        continue

    # 정가 정보가 없으면 정가 = 할인가로 처리 (할인 없음)
    if original_price_int is None:
        original_price_int = sale_price_int

    # 110만원 이하 (할인가 기준)
    if sale_price_int > 1100000:
        continue

    # 할인율 계산
    discount_rate = 0.0
    if original_price_int > 0:
        discount_rate = round(
            (original_price_int - sale_price_int) / original_price_int * 100, 1
        )

    # 터미널에 출력
    print(f"[{idx}]")
    print("상품명 :", name)
    print("쿠폰 :", coupon_text if coupon_text else "정보 없음")
    print("정가(할인 전) :", f"{original_price_int:,}원")
    print("할인가 :", f"{sale_price_int:,}원")
    print("할인율 :", f"{discount_rate:.1f}%")
    print("리뷰수 :", review_count if review_count is not None else "정보 없음")
    print("-" * 40)

    # csv 저장용 데이터 추가
    rows.append([
        name,
        coupon_text if coupon_text else "",
        original_price_int,
        sale_price_int,
        discount_rate,
        review_count if review_count is not None else ""
    ])

# 브라우저 종료
browser.quit()

# csv 파일로 저장
filename = "coupang_notebook.csv"
with open(filename, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["상품명", "쿠폰", "정가", "할인가", "할인율(%)", "리뷰수"])
    writer.writerows(rows)

print(f"\n csv 저장 완료: {filename}")
