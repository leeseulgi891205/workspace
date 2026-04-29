import requests

#url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url = "https://www.melon.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

# 요청 (헤더 포함 버전 사용)
res = requests.get(url,headers=headers)
res.raise_for_status()   # 여기가 맞는 사용법

# 파일 저장
with open("agent3.html", "w", encoding="utf8") as f:
    f.write(res.text)

print("파일이 저장되었습니다")