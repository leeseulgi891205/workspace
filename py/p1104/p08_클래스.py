# 클래스가 2개 있음
# Student클래스, Stuscore클래스
from S_func import *

# 학생성적 들 저장
students = Stuscore()  # 객체선언
students.add(Student(10101,'홍길동',80,80,80))  # 홍길동
students.add(Student(10102,'유관순',90,90,90))  # 유관순
students.add(Student(10103,'이순신',100,100,100))  # 이순신

students.print()