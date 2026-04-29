from django.db import models

class Member(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,default='010-0000-0000')
    gender = models.CharField(max_length=100,default='남자')
    hobby = models.CharField(max_length=100, default='게임')
    mdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user_id},{self.name},{self.phone},{self.hobby},{self.mdate}"
