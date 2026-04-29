# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 1. 기본 정보
    real_name = models.CharField("이름", max_length=30)
    nickname = models.CharField("닉네임", max_length=30, unique=True)
    jumin = models.CharField("주민번호", max_length=20) # 000000-0000000
    phone = models.CharField("휴대폰 번호", max_length=20)
    email = models.EmailField("이메일", max_length=254)
    address = models.CharField("주소", max_length=200, blank=True, null=True)

    # 2. 회원 등급 (무조건 있어야 함)
    GRADE_CHOICES = [
        ('seed', '🌱 새싹회원'),
        ('general', '🌿 일반회원'),
        ('vip', '🌸 우수회원'),
        ('admin', '👑 운영진'),
    ]
    grade = models.CharField("회원 등급", max_length=10, choices=GRADE_CHOICES, default='seed')

    # 3. 성별 (남자/여자)
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
    ]
    gender = models.CharField("성별", max_length=1, choices=GENDER_CHOICES, default='F')

    # 4. 자녀 학급 정보 (없음/초/중/고)
    CHILD_SCHOOL_CHOICES = [
        ('none', '자녀 없음'),
        ('elementary', '초등학생'),
        ('middle', '중학생'),
        ('high', '고등학생'),
    ]
    child_school = models.CharField("자녀 학급", max_length=20, choices=CHILD_SCHOOL_CHOICES, default='none')

    # 약관 동의 여부 (DB 저장용)
    terms_agreed = models.BooleanField("약관 동의", default=False)

    def __str__(self):
        return f"[{self.get_grade_display()}] {self.real_name}"

# 관리자 페이지 분리용 프록시 모델
class GeneralUser(User):
    class Meta:
        proxy = True
        verbose_name = '일반 회원'
        verbose_name_plural = '1. 일반 회원 관리'

class AdminUser(User):
    class Meta:
        proxy = True
        verbose_name = '관리자'
        verbose_name_plural = '2. 관리자(스태프) 관리'