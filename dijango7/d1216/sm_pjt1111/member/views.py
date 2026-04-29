from django.shortcuts import render
from .models import Member

# 로그인
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get('id') # 없을때 None
        pw = request.POST.get('pw') # 없을때 None
        # try: id = request.POST['id'] # 없을때 에러
        # except: id = None
            
        qs = Member.objects.filter(id=id,pw=pw) #없을때 에러나지 않음 => []빈공백
        if qs:
            # 섹션추가
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
            context = {'flag':'1'}
        else:
            context = {'flag':'0','id':id,'pw':pw}
        # try: qs = Member.objects.get(id=id,pw=pw)    #없을때 에러
        # except: qs = None
        
        return render(request,'member/login.html',context)

# 로그아웃
def logout(request):
    request.session.clear()
    context = {'flag':'-1'}
    return render(request,'member/login.html',context)

# 회원가입
def join(request):
    if request.method == 'GET':
        return render(request,'member/join.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        phone3 = request.POST.get('phone3')
        phone = f"{phone1}-{phone2}-{phone3}"
        email = request.POST.get('email')
        post = request.POST.get('post')
        address = request.POST.get('address')
        gender = request.POST.get('gender','남자')
        hobby = request.POST.get('hobby','게임')
        
        # 회원가입 처리
        Member.objects.create(
            id=id,
            pw=pw,
            name=name,
            phone=phone,
            email=email,
            post=post,
            address=address,
            gender=gender,
            hobby=hobby
        )
        
        return render(request,'member/join_complete.html',{'name':name})