from django.shortcuts import render, redirect
from .models import Member

# 로그인
def login(request):
    if request.method == 'GET':
        # 처음 로그인 페이지 들어올 때
        context = {'error': -1}  # 아직 시도 안 함
        return render(request, 'member/login.html', context)
    
    elif request.method == 'POST':
        # 로그인 버튼 눌렀을 때
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        
        # DB에서 일치하는 회원 찾기
        qs = Member.objects.filter(id=id, pw=pw)
        
        if qs.exists():
            context = {'error': 1}  # 로그인 성공
        else:
            context = {'error': 0}  # 로그인 실패
        
        return render(request, 'member/login.html', context)

# 회원 리스트
def list(request):
    # DB에서 모든 회원 가져오기 (최신순)
    qs = Member.objects.all().order_by('-mdate')
    context = {'list': qs}
    return render(request, 'member/list.html', context)

# 회원 등록
def write(request):
    if request.method == 'GET':
        # 회원등록 페이지 보여주기
        return render(request, 'member/write.html')
    
    elif request.method == 'POST':
        # 회원등록 버튼 눌렀을 때
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        hobby_list = request.POST.getlist("hobby")  # 체크박스 여러 개
        hobby_str = ",".join(hobby_list)  # 쉼표로 연결
        
        # DB에 저장
        Member.objects.create(
            id=id,
            pw=pw,
            name=name,
            phone=phone,
            gender=gender,
            hobby=hobby_str
        )
        
        return redirect('/')  # 메인페이지로 이동