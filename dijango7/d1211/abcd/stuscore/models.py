from django.db import models

# 학생 성적을 저장하는 테이블
class Stuscore(models.Model):
    sno = models.AutoField(primary_key=True)  # 번호
    name = models.CharField(max_length=100)   # 이름
    kor = models.IntegerField(default=0)      # 국어 점수
    eng = models.IntegerField(default=0)      # 영어 점수
    math = models.IntegerField(default=0)     # 수학 점수
    total = models.IntegerField(default=0)    # 총점
    avg = models.FloatField(default=0)        # 평균

    def __str__(self):
        return f"{self.sno},{self.name},{self.total}"