from django.shortcuts import render
from .models import Member
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse
import random

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
        return render(request, 'member/join.html')
    elif request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        # 실제 DB 저장
        Member.objects.create(id=userid, pw=password, name=name, phone=phone)
        return render(request, 'member/join.html', {'flag': '1'})

# 이메일 인증번호 발송
@csrf_exempt
def send_email_code(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'soduwkma@naver.com')
        code = str(random.randint(100000, 999999))
        subject = '[VLAST] 회원가입 인증번호'
        message = f'인증번호는 {code} 입니다.'
        send_mail(subject, message, 'noreply@vlashshop.com', [email], fail_silently=False)
        return JsonResponse({'result': 'ok', 'code': code})