from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "회원가입 완료! 바로 로그인 됐음 ✅")
            return redirect("main")
        messages.error(request, "회원가입 실패. 입력값 다시 확인 ㄱ")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "로그인 완료 ✅")
            return redirect("main")
        messages.error(request, "로그인 실패. 아이디/비번 체크 ㄱ")
    else:
        form = LoginForm(request)
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "로그아웃 완료 ✅")
    return redirect("main")
