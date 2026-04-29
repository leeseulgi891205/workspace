import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


## html태그, css문법으로 검색이 가능
# find(), find_all()
# 태그입력시 검색됨.
# text : 태그안에 글자를 출력
#print(soup.find("title")) #타이틀 태그 가져오기
#print(soup.title.text) #타이틀의 글자만 가져오기
#print(soup.a.attrs) #a태그의 속성정보 가져오기
#print(soup.a['href']) #a태그의 href속성값 가져오기
#print(soup.find("div")) #처음나오는 div태그 가져오기
#print(len(soup.find_all("div"))) #검색된 개수
#print(soup.find_all("div")[1].find("div").attrs)
#idHeader = soup.find("div",{"id":"header"})
#print(idHeader.find("h1",{"class":"search_logo"}))
#print(soup.find("legend",{"class":"blind"}))
print(soup.find("legend",class_="blind"))
print(soup.find("div",id="header"))






#--------------------------------------------------
#파일저장
#with open("naver1.html","w",encoding="utf8") as f:
#    f.write(res.text)
    
#with open("naver2.html","w",encoding="utf8") as f:
#    f.write(soup.prettify())
    
#print("파일이 저장되었습니다")