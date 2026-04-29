from django.shortcuts import render, redirect

def login(request):
    if request.method == 'GET':
        
        # 쿠키 검색
        cooksave_id = request.COOKIES.get('cooksave_id', '')
        context = {'cooksave_id': cooksave_id}
        return render(request, 'member/login.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        login_keep = request.POST.get('login_keep')    # getlist()
        
        # 쿠키읽기
        print("모든 쿠키 읽기 :",request.COOKIES)
        
        # 쿠키저장
        response = redirect('/')
        if login_keep:
            print("아이디 저장이 체크가 되었습니다.")
            ## 쿠키에 아이디 저장시켜줌.
            response.set_cookie("cooksave_id", id, max_age=60*60*24*30) # 30일간 유지
            
        else:
            print("아이디 저장이 체크가 해제 되었습니다.")
            response.delete_cookie("cooksave_id")
        
        return response
        
