from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .forms import SignUpForm

# 1. 회원가입
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/') 
        else:
            print("회원가입 실패:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup/signup.html', {'form': form})

# 2. 로그인 (★ 수정된 부분)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 여기서 is_locked 체크 로직을 제거했습니다.
            login(request, form.get_user())
            return redirect('/')
        else:
            # 로그인 실패 시 다시 입력 화면으로 (에러 메시지 포함)
            return render(request, 'accounts/login/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login/login.html', {'form': form})

# 3. 로그아웃
def logout_view(request):
    logout(request)
    return redirect('/')

# 4. 아이디 중복 확인
# accounts/views.py 맨 아래

def check_id(request):
    username = request.GET.get('username')
    User = get_user_model()
    try:
        if User.objects.filter(username=username).exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})
    except Exception as e:
        print(f"ID Check Error: {e}")
        return JsonResponse({'exists': True})


# ★ 비밀번호 찾기 페이지
def find_pw(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        try:
            User = get_user_model()
            user = User.objects.get(username=username, email=email)
            
            # 임시 비밀번호 생성
            import random
            import string
            temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            
            # 비밀번호 변경
            user.set_password(temp_password)
            user.save()
            
            # 이메일 발송
            from django.core.mail import send_mail
            from django.conf import settings
            
            subject = '[맘스로그] 임시 비밀번호 발급 안내'
            message = f'''
안녕하세요, {user.real_name}님

임시 비밀번호가 발급되었습니다.

아이디: {user.username}
임시 비밀번호: {temp_password}

로그인 후 반드시 비밀번호를 변경해 주세요.

감사합니다.
맘스로그 드림
            '''
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                context['found'] = True
            except Exception as e:
                print(f"이메일 발송 실패: {e}")
                context['error'] = f"임시 비밀번호 생성에는 성공했으나 이메일 발송에 실패했습니다. 관리자에게 문의하세요. (임시 비밀번호: {temp_password})"
            
        except User.DoesNotExist:
            context['error'] = "입력하신 아이디와 이메일이 일치하는 회원 정보를 찾을 수 없습니다."
    
    return render(request, 'accounts/find_pw.html', context)

# accounts/views.py 맨 아래

# accounts/views.py (맨 아래에 추가)

def find_id(request):
    context = {}
    if request.method == 'POST':
        real_name = request.POST.get('real_name')
        email = request.POST.get('email')
        
        try:
            # 이름과 이메일이 일치하는 회원 찾기
            User = get_user_model()
            user = User.objects.get(real_name=real_name, email=email)
            context['found_id'] = user.username # 찾은 아이디를 담음
        except User.DoesNotExist:
            context['error'] = "일치하는 회원 정보를 찾을 수 없습니다."
            
    return render(request, 'accounts/find_id.html', context)

# 1. 비밀번호 확인 (검문소)
@login_required
def profile_auth(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        
        # 비밀번호가 맞는지 확인
        if request.user.check_password(password):
            request.session['is_verified'] = True
            return redirect('accounts:profile')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
    
    return render(request, 'accounts/profile_auth.html')

# 2. 진짜 마이페이지
@login_required
def profile(request):
    # 검문 통과 안 했으면 검문소로 보냄
    if not request.session.get('is_verified'):
        return redirect('accounts:profile_auth')
    
    return render(request, 'accounts/profile.html')





