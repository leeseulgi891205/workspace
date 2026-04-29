from django.contrib import admin
from .models import Student  # 같은 폴더에 있는 models.py 에서 Student 가져오기

# admin 사이트에 Student 테이블을 등록
# 이렇게 해야 /admin 페이지에서 Student 데이터를 볼 수 있다.
admin.site.register(Student)