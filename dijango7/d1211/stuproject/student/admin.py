from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name_link', 'major', 'age', 'grade', 'created_at']
    list_filter = ['major', 'grade']
    search_fields = ['name', 'major']
    
    def name_link(self, obj):
        url = reverse('student:view', args=[obj.pk])
        return format_html('<a href="{}">{}</a>', url, obj.name)
    name_link.short_description = '이름'
