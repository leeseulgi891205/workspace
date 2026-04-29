import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

trs = soup.find("div",{"class":"box_type_l"}).table.find_all("tr")
#print(trs[2].find_all("td")[1].text)
#print(trs[11].find_all("td")[3].text)
for td in trs[11].find_all("td"):
    print(td.text.strip(),end="\t")
    

    
for td in trs:
    print(td.get_text(strip=True))
trs = soup.find_all("th")
for th in trs:
    print(th.get_text(strip=True))
    
for tr in trs:
    tds = tr.find_all("td")
    if len(tds) == 0:
        continue
    for td in tds:
        text = td.get_text(strip=True)
        print(text)
print("----- 줄 끝 -----")
   






#print(len(trs))




#print(soup.prettify())
# 파일저장 ---------------------------------------------------------------
#with open("stock.html","w",encoding="utf8") as f:
#    f.write(soup.prettify())
    
#print("파일이 저장되었습니다")