from django.contrib import admin
from django.urls import path, include

# 다른 app에 있는 url들을 포함시키기 위해 include 함수를 사용합니다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls') ),
    # home 앱의 urls.py를 포함시킵니다.
    path('', include('home.urls') ),
]
