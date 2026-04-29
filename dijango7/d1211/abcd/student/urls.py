from django.urls import path
from . import views   # 같은 폴더의 views.py 불러오기

# 템플릿에서 {% url 'student:write' %} 이런 식으로 부를 때 쓰는 이름
app_name = 'student'

urlpatterns = [
    # /student/list/ 로 들어오면 views.list 함수 실행
    path('list/', views.list, name='list'),

    # /student/write/ 로 들어오면 views.write 함수 실행
    path('write/', views.write, name='write'),

    # /student/view/1/ 처럼 숫자를 같이 보내서 상세보기
    #  : 정수형 sno 값을 views.view 함수의 인자로 넘긴다.
    path('view//', views.view, name='view'),

    # /student/delete/1/ 처럼 들어오면 sno가 1인 학생을 삭제 (완성 버전)
    path('delete//', views.delete, name='delete'),
]