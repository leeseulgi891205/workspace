from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import datetime

# 로그인 부분
def login(request):
    if request.method == 'GET':
        # 쿠키 읽어와서 context로 저장해서 전달
        cook_id = request.COOKIES.get("cook_id","")     # 없으면 빈공백전송
        cook_pw = request.COOKIES.get("cook_pw","")     # 비밀번호 쿠키
        context = {'cook_id':cook_id, 'cook_pw':cook_pw}
        return render(request, 'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        login_keep = request.POST.get("login_keep")
        # id,pw를 활용해서 로그인체크
        qs = Member.objects.filter(id=id,pw=pw)
        if qs:
            print("id,pw 일치 : ",id,pw)
            # 세션저장
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
            context = {"state_code":"1"}
            response = render(request, 'member/login.html', context)
            
            # 쿠키저장
            if login_keep:
                response.set_cookie("cook_id", id, max_age=60*60*24*30)
                response.set_cookie("cook_pw", pw, max_age=60*60*24*30)
            else:
                # 쿠키삭제
                response.delete_cookie("cook_id")
                response.delete_cookie("cook_pw")
            
            return response
            
        else:
            print("id,pw 불일치")
            context = {"state_code":"0"}
            return render(request, 'member/login.html', context)


# 로그아웃 부분
def logout(request):
    # 섹션 모두 삭제
    request.session.clear()
    
    context = {"state_code":"-1"}
    return render(request, 'member/login.html', context)

# 회원등록 부분
def join(request):
    if request.method == 'GET':
        return render(request, 'member/join.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        hobby = ','.join(request.POST.getlist("hobby"))
        zipcode = request.POST.get("zipcode", "")
        address = request.POST.get("address", "")
        addressdetail = request.POST.get("addressdetail", "")
        profile_image = request.FILES.get("profile_image")
        
        Member.objects.create(
            id=id, pw=pw, name=name, phone=phone, gender=gender, hobby=hobby,
            zipcode=zipcode, address=address, addressdetail=addressdetail,
            profile_image=profile_image
        )
        
        context = {"join_state":"1"}
        return render(request, 'member/login.html', context)

# 회원리스트 부분
def list(request):
    qs = Member.objects.all().order_by('-mdate')
    context = {"list":qs}
    return render(request, 'member/list.html', context)

# 엑셀 다운로드 부분
def excel_download(request):
    
    wb = Workbook()
    ws = wb.active
    ws.title = "회원리스트"
    
    # 헤더 설정
    headers = ['아이디', '비밀번호', '이름', '전화번호', '우편번호', '주소', '상세주소', '성별', '취미', '가입일']
    ws.append(headers)
    
    # 헤더 스타일 설정
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')
    
    # 데이터 추가
    members = Member.objects.all().order_by('-mdate')
    for member in members:
        ws.append([
            member.id,
            member.pw,
            member.name,
            member.phone,
            member.zipcode,
            member.address,
            member.addressdetail,
            member.gender,
            member.hobby,
            member.mdate.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    # 열 너비 조정
    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 12
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 12
    ws.column_dimensions['F'].width = 35
    ws.column_dimensions['G'].width = 30
    ws.column_dimensions['H'].width = 10
    ws.column_dimensions['I'].width = 30
    ws.column_dimensions['J'].width = 20
    
    # HTTP 응답 생성
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="member_list_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx"'
    wb.save(response)
    
    return response

# 회원수정 부분
def update(request, id):
    if request.method == 'GET':
        member = Member.objects.get(id=id)
        context = {"member": member}
        return render(request, 'member/update.html', context)
    elif request.method == 'POST':
        member = Member.objects.get(id=id)
        member.pw = request.POST.get("pw")
        member.name = request.POST.get("name")
        member.phone = request.POST.get("phone")
        member.gender = request.POST.get("gender")
        member.hobby = ','.join(request.POST.getlist("hobby"))
        member.zipcode = request.POST.get("zipcode", "")
        member.address = request.POST.get("address", "")
        member.addressdetail = request.POST.get("addressdetail", "")
        profile_image = request.FILES.get("profile_image")
        if profile_image:
            member.profile_image = profile_image
        member.save()
        
        return render(request, 'member/update.html', {"member": member, "update_state": "1"})

# 회원삭제 부분
def delete(request, id):
    Member.objects.get(id=id).delete()
    qs = Member.objects.all().order_by('-mdate')
    context = {"list": qs, "delete_state": "1"}
    return render(request, 'member/list.html', context)

# 회원상세보기 부분
def detail(request, id):
    member = Member.objects.get(id=id)
    context = {"member": member}
    return render(request, 'member/detail.html', context)

# 아이디 찾기 부분
def find_id(request):
    if request.method == 'GET':
        return render(request, 'member/find_id.html')
    elif request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        
        # 이름과 전화번호로 회원 찾기
        try:
            member = Member.objects.get(name=name, phone=phone)
            # 아이디 전체 표시
            context = {"find_state": "1", "masked_id": member.id, "mdate": member.mdate}
            return render(request, 'member/find_id.html', context)
        except Member.DoesNotExist:
            context = {"find_state": "0"}
            return render(request, 'member/find_id.html', context)

# 비밀번호 찾기 부분
def find_pw(request):
    if request.method == 'GET':
        return render(request, 'member/find_pw.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        
        # 아이디, 이름, 전화번호로 회원 찾기
        try:
            member = Member.objects.get(id=id, name=name, phone=phone)
            # 비밀번호 전체 표시
            context = {"find_state": "1", "password": member.pw, "id": member.id}
            return render(request, 'member/find_pw.html', context)
        except Member.DoesNotExist:
            context = {"find_state": "0"}
            return render(request, 'member/find_pw.html', context)