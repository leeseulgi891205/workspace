from django.shortcuts import render, redirect      # 화면 보여주기 + 다른 URL로 이동
from django.urls import reverse                   # URL 이름을 실제 주소로 바꿔주는 함수
from .models import Stuscore                      # 성적 모델 불러오기

# -----------------------------
# 성적 입력 (화면 + 저장)
# -----------------------------
def write(request):
    # 1) GET 요청: 화면만 보여줄 때
    if request.method == 'GET':
        # stuscore/write.html 템플릿만 보여준다.
        return render(request, 'stuscore/write.html')

    # 2) POST 요청: 폼에서 '등록' 버튼을 눌렀을 때
    elif request.method == 'POST':
        # 입력값 꺼내기
        name = request.POST.get('name')      # 이름
        kor = request.POST.get('kor')        # 국어 점수 (문자열 형태)
        eng = request.POST.get('eng')        # 영어 점수
        math = request.POST.get('math')      # 수학 점수

        # 화면에서 들어온 값은 문자열(str)이므로, 정수(int)로 변환
        # int('90') → 90
        kor = int(kor)
        eng = int(eng)
        math = int(math)

        # 총점과 평균 계산
        total = kor + eng + math
        avg = total / 3   # 파이썬 나눗셈은 실수(float)로 결과가 나온다.

        # Stuscore 객체 만들고 DB에 저장
        Stuscore(
            name=name,
            kor=kor,
            eng=eng,
            math=math,
            total=total,
            avg=avg,
        ).save()

        # 저장 후 성적 리스트 페이지로 이동
        return redirect(reverse('stuscore:list'))


# -----------------------------
# 성적 리스트 (전체 성적 보기)
# -----------------------------
def list(request):
    # Stuscore 테이블의 모든 데이터 가져오기
    # 최신 입력이 위로 오게 sno 내림차순 정렬
    qs = Stuscore.objects.all().order_by('-sno')

    # 템플릿에 넘길 데이터 딕셔너리
    context = {
        'list': qs,
    }

    # stuscore/list.html 에 list 데이터와 함께 전달
    return render(request, 'stuscore/list.html', context)
