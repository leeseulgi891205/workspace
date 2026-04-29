# board/views.py
from django.shortcuts import render
from .models import Notice

# 1. 메인 페이지: 그냥 깔끔한 환영 인사만 보여줍니다. (데이터 조회 X)
def main(request):
    return render(request, 'main.html')

# 2. 공지사항 페이지: 여기서 DB 데이터를 가져옵니다.
def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    context = {
        'notices': notices
    }
    return render(request, 'notice_list.html', context)