from django.db import models

class student(models.Model):
    # 테이블 생성 - 파이썬 명령어로 sql문을 대체해서 생성 ORM 방식
    id = models.CharField(max_length=100, primary_key=True)
    pw = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=10)
    hobby = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id},{self.name},{self.age},{self.gender},{self.phone},{self.hobby}"