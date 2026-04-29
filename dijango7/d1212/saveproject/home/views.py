from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # 쿠키 읽어오기 - request.COOKIES 사용
    # 쿠키 저장 - response.set_cookie() 사용
    
    # 쿠키 검색 - request.COOKIES.get('쿠키이름')
    cook_info = request.COOKIES
    print("쿠키 정보 : ",cook_info)
    cook_id = request.COOKIES.get('cook_id', '')            # cook_id, 없으면 빈 공백처리
    print("cook_id 정보: ",cook_id)
    
    
    response = render(request, 'index.html')
    ## 쿠키 저장 - response
    # cook_id = aaa
    # 유지시간이 없으면, 브라우저 종료시까지 유지, 시간을 설정하면 시간동안 유지가 됨
    # 쿠키정보가 없을때만 쿠키 저장
    # if not cook_id:
    #     response.set_cookie("smsite_connect", "ok")  
    #     response.set_cookie("ip", "127.0.0.1:8000",max_age=86400)
    
        
        
    return response
    
    
    
    #
