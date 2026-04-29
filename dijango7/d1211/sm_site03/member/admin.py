from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'gender', 'hobby', 'mdate']
    list_filter = ['gender', 'mdate']
    search_fields = ['id', 'name', 'phone']
    readonly_fields = ['mdate']
