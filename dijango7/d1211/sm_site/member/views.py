from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Member

# 회원등록 페이지
def write(request):
    if request.method == 'GET':
        return render(request, 'member/write.html')
    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        pw = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        hobby = request.POST.get('hobby' )
        
        Member.objects.create(
            user_id=user_id,
            pw=pw,
            name=name,
            phone=phone,
            gender=gender,
            hobby=hobby
        )
        return redirect('member:list')

# 회원리스트 페이지
def member_list(request):
    
    members = Member.objects.all().order_by('-mdate')
    context = {'members': members}
    return render(request, 'member/list.html', context)

# 로그인 페이지
def login(request):
    if request.method == 'GET':
        return render(request, 'member/login.html')
    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        pw = request.POST.get('password')
        try:
            member = Member.objects.get(user_id=user_id, pw=pw)
            request.session['session_id'] = member.user_id
            request.session['session_name'] = member.name
            return redirect('home_index')
        except Member.DoesNotExist:
            return HttpResponse("아이디 또는 비밀번호가 일치하지 않습니다.")

# 로그아웃
def logout(request):
    request.session.clear()
    return redirect('home_index')
