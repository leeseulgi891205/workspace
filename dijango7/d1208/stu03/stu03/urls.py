from django.contrib import admin
from django.urls import path, include

# url을 student 앱으로 연결
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('student/', include('student.urls')),
]
