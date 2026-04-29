from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate
from .forms import PasswordConfirmForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "회원가입 완료! 바로 시작해보자 😎")
            return redirect('pages:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "로그인 성공!")
            return redirect('pages:home')
        else:
            messages.error(request, "로그인 실패. 아이디/비번 확인 ㄱㄱ")
    else:
        form = LoginForm(request)
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "로그아웃 완료.")
    return redirect('pages:home')

# 비밀번호 확인 후 마이페이지 이동(251222)
@login_required
def profile_view(request):
    if request.method == 'POST': # POST: 비밀번호 제출 후 authenticate로 확인
        form = PasswordConfirmForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(username=request.user.username, password=password)
            if user:
                # 비밀번호 확인 완료 → 실제 프로필 렌더
                return render(request, 'accounts/profile.html')  
                # 틀리면 에러 메시지 표시
            else:
                form.add_error('password', '비밀번호가 틀렸습니다.')
    else: # GET: 비밀번호 입력 폼 렌더
        form = PasswordConfirmForm()
    
    return render(request, 'accounts/profile_confirm.html', {'form': form})
