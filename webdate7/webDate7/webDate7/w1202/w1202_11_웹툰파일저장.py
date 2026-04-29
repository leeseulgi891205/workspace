import requests
from bs4 import BeautifulSoup
import os
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

url="https://comic.naver.com/index"
# selenium 함수호출

# 파일 불러오기
with open("webtoon_browser.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

# 실시간 신작 랭킹 ---------------------------------
aside = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# 실시간 신작 랭킹 - wraps[1]
wraps = aside.find_all("div",{"class":"component_wrap"})
# 5개 인기웹툰 내용
lis = wraps[1].find_all("li")
print('[ 실시간 신작 랭킹 ]')
for i,li in enumerate(lis):
    print(li.find("img")['src'])
    # request url정보를 가져옴. jpg -> jpg정보를 가져옴.
    img_req = requests.get(li.find("img")['src'],headers=headers)
    os.makedirs("webtoon",exist_ok=True) # 폴더가 없을때만 생성됨.
    # if not os.isdir("webtoon"):
    #     os.makedirs("webtoon") 
    # 파일 저장
    with open(f"webtoon/webtoon_{i+1}.jpg","wb") as f:
        f.write(img_req.content) #파일로 저장
    print(li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text.strip())
    print(li.find("span",{"class":"text"}).text.strip())
    print(li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text.strip())
    print("-"*50)



# # 실시간 인기웹툰 ---------------------------------
# aside = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# # 실시간 인기웹툰 - wraps[0]
# wraps = aside.find_all("div",{"class":"component_wrap"})
# # 5개 인기웹툰 내용
# lis = wraps[0].find_all("li")
# # 1번째 등수,제목,작가
# print("[ 실시간 인기 웹툰 리스트 ]")
# for i,li in enumerate(lis):
#     print(li.find("img")['src'])
    
#     image_res = requests.get(li.find("img")['src'],headers=headers)
#     with open(f"webtoon_{i}.jpg","wb") as f:
#         f.write(image_res.content)
#     print(li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text.strip())
#     print(li.find("span",{"class":"text"}).text.strip())
#     print(li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text.strip())
#     print("-"*50)




# for i in range(5):
#     print(lis[i].find("strong",{"class":"AsideList__ranking--sNPZy"}).text.strip())
#     print(lis[i].find("span",{"class":"text"}).text.strip())
#     print(lis[i].find("a",{"class":"ContentAuthor__author--CTAAP"}).text.strip())



# # 실시간 인기웹툰 ---------------------------------
# aside = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# # 실시간 인기웹툰 위치검색
# wraps = aside.find_all("div",{"class":"component_wrap"})
# # 웹툰 5개
# lis = wraps[0].find("ul").find_all("li")
# # 각각의 제목 출력
# print(lis[0].find("strong",{"class":"AsideList__ranking--sNPZy"}).text.strip())
# print(lis[0].find("span",{"class":"text"}).text.strip())
# print(lis[0].find("a",{"class":"ContentAuthor__author--CTAAP"}).text.strip())




   
   
# 상단메뉴 출력 ----------------------------    
# ul = soup.find("ul",{"id":"menu"})
# lis = ul.find_all("li")
# for li in lis:
#     print(li.a.text.strip())
    
# print(lis[0].text.strip())
# print(lis[1].text.strip())
# print(lis[2].text.strip())
# print(lis[3].text.strip())
# print(lis[4].text.strip())
# print(lis[5].text.strip())

   