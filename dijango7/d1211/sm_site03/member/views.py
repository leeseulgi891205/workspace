from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Member

# 로그인
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        print("post 입력 : ",id,pw)
        qs = Member.objects.filter(id=id,pw=pw)
        if qs:
            print("아이디와 비밀번호가 일치합니다")
            error = 0
            return redirect("/")
        else:
            print("아이디와 비밀번호가 일치하지 않습니다")
            context = {"error":"0"}
            return render(request,'member/login.html',context)
    
    
# 회원전체리스트페이지
def list(request):
    qs = Member.objects.all().order_by('-mdate')
    context = {"list":qs}
    return render(request,'member/list.html',context)

# 회원상세보기
def view(request, id):
    member = Member.objects.get(id=id)
    context = {"member":member}
    return render(request,'member/view.html',context)



# 회원등록페이지
def write(request):
    if request.method == 'GET':
        return render(request,'member/write.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        image = request.FILES.get("image")
        
        Member.objects.create(
           id=id,pw=pw,name=name,phone=phone,gender=gender,hobby=hobby,image=image
        )
        print("post 확인 : ",id)
        return redirect('/member/list/')

# 회원수정페이지
def update(request, id):
    member = Member.objects.get(id=id)
    if request.method == 'GET':
        context = {"member":member}
        return render(request,'member/update.html',context)
    elif request.method == 'POST':
        member.pw = request.POST.get("pw")
        member.name = request.POST.get("name")
        member.phone = request.POST.get("phone")
        member.gender = request.POST.get("gender")
        member.hobby = ','.join(request.POST.getlist("hobby"))
        
        if request.FILES.get("image"):
            member.image = request.FILES.get("image")
        
        member.save()
        return redirect('/member/list/')

# 회원삭제
def delete(request, id):
    Member.objects.get(id=id).delete()
    return redirect('/member/list/')