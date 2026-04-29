from django.shortcuts import render
from django.http import JsonResponse
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
        return render(request,'member/회원가입95.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        gender = request.POST.get('gender','남자')
        hobby = request.POST.get('hobby','')
        post = request.POST.get('post','')
        address = request.POST.get('address','')
        address_detail = request.POST.get('address_detail','')
        
        # 아이디 중복 확인
        if Member.objects.filter(id=id).exists():
            context = {'flag':'0','id':id}
            return render(request,'member/회원가입95.html',context)
        
        # 회원 생성
        Member.objects.create(
            id=id,
            pw=pw,
            name=name,
            phone=phone,
            email=email,
            gender=gender,
            hobby=hobby,
            post=post,
            address=address,
            address_detail=address_detail
        )
        
        return render(request,'member/회원가입완료.html',{'name':name})

# 아이디 중복확인
def check_id(request):
    id = request.GET.get('id','')
    if not id:
        return JsonResponse({'result': 'error', 'msg': '아이디를 입력하세요.'})
    
    # 아이디 중복 체크
    if Member.objects.filter(id=id).exists():
        return JsonResponse({'result': 'duplicate', 'msg': '이미 사용중인 아이디입니다.'})
    else:
        return JsonResponse({'result': 'available', 'msg': '사용 가능한 아이디입니다.'})

# 회원목록
def member_list(request):
    members = Member.objects.all().order_by('-mdate')
    context = {'members': members}
    return render(request, 'member/member_list.html', context)

# 회원 상세보기
def member_view(request, id):
    member = Member.objects.get(id=id)
    context = {'member': member}
    return render(request, 'member/member_view.html', context)