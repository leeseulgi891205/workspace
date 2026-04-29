from django.db import models

# Student 클래스 = 학생 테이블 설계도
# models.Model 을 상속받으면, 장고가 이 클래스를 보고 실제 DB 테이블을 만들어줌.
class Student(models.Model):
    # sno : 학생 번호. 1, 2, 3... 자동 증가. primary_key=True → 기본키(고유값)로 사용
    sno = models.AutoField(primary_key=True)

    # name : 학생 이름. 최대 100글자까지 저장 가능
    name = models.CharField(max_length=100)

    # age : 나이. 정수형. 기본값 1
    age = models.IntegerField(default=1)

    # grade : 학년. 정수형
    grade = models.IntegerField(default=1)

    # gender : 성별. "남자", "여자" 같은 문자열 들어갈 예정
    gender = models.CharField(max_length=10)

    # hobby : 취미. 문자열 저장. 기본값은 '게임'
    hobby = models.CharField(max_length=100, default='게임')

    # 이 객체를 문자열로 보여줄 때 어떻게 보일지 설정
    # 예: admin 페이지나 쉘에서 Student 객체를 출력하면 이 내용이 보임
    def __str__(self):
        # f문자열 : f"문자 {변수}" 형태
        return f"{self.sno},{self.name},{self.age},{self.grade},{self.gender}"