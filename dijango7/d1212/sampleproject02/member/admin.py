from django.contrib import admin
from .models import Member

# 관리자화면 등록
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'pw', 'name', 'phone', 'gender', 'hobby', 'zipcode', 'address', 'addressdetail', 'profile_image', 'mdate']
    list_filter = ['gender', 'mdate']
    search_fields = ['id', 'name', 'phone']
    readonly_fields = ['mdate']
