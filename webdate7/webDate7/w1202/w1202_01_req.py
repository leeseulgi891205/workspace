import requests

#res = requests.get("https://www.naver.com")
#url = "https://www.naver.com"
url = "https://www.google.com"
res = requests.get(url)
#status_code: 200(정상), 403(권한없음), 404(페이지없음), 500(서버에러),raose_for_status() : 응답코드가 200이 아니면 예외 발생
res.raise_for_status()  # 문제시 예외 발생 에러시 프로그램 종료

print("응답코드: ",res.status_code)
print(requests.codes.ok)  # 200
#print(res.text)