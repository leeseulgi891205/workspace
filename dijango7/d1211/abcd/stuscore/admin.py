from django.contrib import admin
from .models import Stuscore

# 관리자 페이지에서 성적 관리 가능하도록 등록
admin.site.register(Stuscore)