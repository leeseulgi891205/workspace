from django.db import models

class Member(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13,default='010-0000-0000')
    email = models.EmailField(max_length=100,default='',blank=True)
    gender = models.CharField(max_length=10,default='남자')
    hobby = models.CharField(max_length=100,default='게임')
    post = models.CharField(max_length=10,default='',blank=True)  # 우편번호
    address = models.CharField(max_length=200,default='',blank=True)  # 주소
    address_detail = models.CharField(max_length=200,default='',blank=True)  # 상세주소
    mdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id},{self.name},{self.hobby},{self.mdate}"

