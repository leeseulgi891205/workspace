from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('남자', '남자'),
        ('여자', '여자'),
    ]
    
    sno = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50, unique=True, default='user', verbose_name='아이디')
    password = models.CharField(max_length=100, default='1234', verbose_name='비밀번호')
    name = models.CharField(max_length=100, verbose_name='이름')
    nickname = models.CharField(max_length=50, default='익명', verbose_name='닉네임')
    email = models.EmailField(max_length=100, default='user@example.com', verbose_name='이메일')
    phone = models.CharField(max_length=20, default='000-0000-0000', verbose_name='전화번호')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='남자', verbose_name='성별')
    age = models.IntegerField(default=1, verbose_name='나이')
    grade = models.IntegerField(default=1, verbose_name='학년')
    hobby = models.CharField(max_length=100, default='게임', verbose_name='취미')
    
    class Meta:
        ordering = ['sno']  # 순서 정렬
        verbose_name = '학생'
        verbose_name_plural = '학생들'
    
    def __str__(self):
        return f"{self.sno}. {self.name} ({self.user_id})"
