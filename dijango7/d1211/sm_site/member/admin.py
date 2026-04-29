from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'phone', 'gender', 'hobby', 'mdate']
    list_filter = ['gender', 'mdate']
    search_fields = ['user_id', 'name', 'phone']
    ordering = ['-mdate']

