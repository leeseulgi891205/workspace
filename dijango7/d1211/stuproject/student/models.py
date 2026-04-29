from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='이름')
    major = models.CharField(max_length=100, verbose_name='전공')
    age = models.IntegerField(verbose_name='나이')
    grade = models.IntegerField(verbose_name='학년')
    address = models.CharField(max_length=200, verbose_name='주소', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    
    def __str__(self):
        return f'{self.name} ({self.major})'
    
    class Meta:
        verbose_name = '학생'
        verbose_name_plural = '학생 목록'
        ordering = ['-created_at']
