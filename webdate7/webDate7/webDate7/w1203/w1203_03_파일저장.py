import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv

fileName = "1.csv"
title = ["제목,평점,날짜"]
date1 = ["안녕1",9.1,"2025-01-01"]
date2 = ["안녕2",9.2,"2025-02-02"]
date3 = ["안녕3",9.3,"2025-03-03"]


# 파일 csv 저장방법
# CSV파일로 저장시 utf-8-sig로 저장해야 한글깨짐 방지 newline="" 옵션 추가해야 행간격 벌어짐 방지
f = open(fileName,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

writer.writerow(title)
writer.writerow(date1)
writer.writerow(date2)
writer.writerow(date3)

f.close()
print("파일생성완료")



