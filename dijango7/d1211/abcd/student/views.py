from django.shortcuts import render, redirect      # render: 화면 보여주기, redirect: 다른 URL로 이동
from django.urls import reverse                   # reverse: URL 이름 → 실제 주소로 변환
from .models import Student                       # Student 모델 불러오기

# -----------------------------
# 학생 등록 (입력 폼 + 저장)
# -----------------------------
def write(request):
    # 1) GET 요청 : 화면만 보여줄 때
    if request.method == 'GET':
        # student/write.html 템플릿을 화면에 보여줌
        return render(request, 'student/write.html')

    # 2) POST 요청 : 폼에서 "등록" 버튼을 눌렀을 때
    elif request.method == 'POST':
        # 화면에서 넘어온 값 꺼내기
        # name="..." 과 같은 이름으로 넘어온다.
        name = request.POST.get('name')      # 이름
        age = request.POST.get('age')        # 나이
        grade = request.POST.get('grade')    # 학년
        gender = request.POST.get('gender')  # 성별

        # checkbox는 여러 개가 선택될 수 있으므로 getlist() 사용
        hobby_list = request.POST.getlist('hobby')  # ['게임', '독서'] 이런 식으로 리스트로 옴

        # 리스트를 "게임,독서" 이런 문자열로 합치기
        hobby = ','.join(hobby_list)

        # Student 객체 하나 생성 후 DB에 저장
        Student(
            name=name,
            age=age,
            grade=grade,
            gender=gender,
            hobby=hobby,
        ).save()

        # 저장 후에는 학생 리스트 페이지로 보내기
        # reverse('student:list') → '/student/list/' 이런 실제 주소로 변환
        return redirect(reverse('student:list'))


# -----------------------------
# 학생 리스트 (전체 목록 보기)
# -----------------------------
def list(request):
    # Student.objects.all() : Student 테이블의 모든 데이터 가져오기
    # .order_by('-sno', 'name') : sno 기준 내림차순 → 같은 sno면 name 순
    qs = Student.objects.all().order_by('-sno', 'name')

    # 템플릿에 넘겨줄 데이터 딕셔너리
    context = {
        'list': qs,
    }

    # student/list.html 템플릿을 화면에 보여주면서, context 데이터 같이 전달
    return render(request, 'student/list.html', context)


# -----------------------------
# 학생 상세보기
# -----------------------------
def view(request, sno):
    # sno에 해당하는 학생 한 명만 가져오기
    # primary_key이므로 값이 없으면 에러, 반드시 한 명이어야 함
    student = Student.objects.get(sno=sno)

    context = {
        'student': student,
    }

    # student/view.html 화면에 한 명 정보 보여주기
    return render(request, 'student/view.html', context)


# -----------------------------
# 학생 삭제 (완성된 버전)
# -----------------------------
def delete(request, sno):
    """
    학생을 삭제하는 함수.

    1) URL에서 sno(학생번호)를 받는다.
    2) 그 번호에 해당하는 Student 객체를 DB에서 가져온다.
    3) delete() 를 호출해서 실제 DB에서 삭제한다.
    4) 삭제 후에는 학생 리스트 페이지로 이동시킨다.
    """

    # sno에 해당하는 학생 한 명 가져오기
    student = Student.objects.get(sno=sno)

    # 실제로 DB에서 삭제
    student.delete()

    # 삭제 후, 다시 학생 리스트 페이지로 이동
    # reverse('student:list') → '/student/list/' 로 변환
    return redirect(reverse('student:list'))