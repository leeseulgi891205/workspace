from django.shortcuts import render
import requests
import json

def index(request):
    # KOBIS 영화진흥위원회 API 접속
    kobis_key = 'c3010f63ec81e3e1b75c3c94ce850ef7'
    target_dt = '20251218'  # 어제 날짜
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={kobis_key}&targetDt={target_dt}'
    
    try:
        # 영화 박스오피스 정보 가져오기
        rel = requests.get(url)
        json_data = json.loads(rel.text)
        movie_list = json_data['boxOfficeResult']['dailyBoxOfficeList'][:5]  # 상위 5개만
    except:
        movie_list = []
    
    context = {'movie_list': movie_list, 'targetDt': target_dt}
    return render(request,'index.html', context)
