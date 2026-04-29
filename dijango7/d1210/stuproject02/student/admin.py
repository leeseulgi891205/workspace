from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno', 'user_id', 'name', 'nickname', 'email', 'phone', 'gender', 'age', 'grade']
    list_display_links = ['sno', 'user_id', 'name']
    list_filter = ['gender', 'grade']
    search_fields = ['user_id', 'name', 'nickname', 'email', 'phone']
    ordering = ['sno']
    
    fieldsets = [
        ('기본 정보', {'fields': ['user_id', 'password', 'name', 'nickname']}),
        ('연락처 정보', {'fields': ['email', 'phone']}),
        ('개인 정보', {'fields': ['gender', 'age', 'grade', 'hobby']}),
    ]
