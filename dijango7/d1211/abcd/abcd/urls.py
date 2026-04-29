from django.contrib import admin              # 관리자(admin) 사이트용
from django.urls import path, include         # path: URL 패턴, include: 다른 urls.py 불러오기

# 이 파일은 "큰길 안내판"이라고 생각하면 됨.
# 어떤 주소로 들어오면 어느 앱으로 보내줄지 적어 둔다.
urlpatterns = [
    # /admin/ 으로 들어오면 장고 기본 관리자 페이지로 연결
    path('admin/', admin.site.urls),

    # / 로 들어오면 home 앱 안의 urls.py 에게 넘김
    path('', include('home.urls')),

    # /student/ 로 시작하는 주소는 student 앱으로
    path('student/', include('student.urls')),

    # /stuscore/ 로 시작하는 주소는 stuscore 앱으로
    path('stuscore/', include('stuscore.urls')),
]
