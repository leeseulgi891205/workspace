import requests
from bs4 import BeautifulSoup

url = ""
headers = {"User-Agent": ""}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")