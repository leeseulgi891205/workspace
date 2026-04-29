# 클래스 선언
# __init__함수사용
class Student:
    def __init__(self,stuno,name,kor,eng,math): # 생성자 - 객체선언시 바로 실행되는 함수
        # 클래스사용하는 전역변수 = 함수내에 사용하는 지역변수
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
    # 합계
    def total_f(self):
        self.total = self.kor+self.eng+self.math
    # 평균
    def avg_f(self):
        self.avg = self.total/3          

# 매개변수 __init__함수 매개변수 개수와 맞아야 함. 5개를 넘겨줘야 함.
s = Student(10101,'홍길동',80,80,80)
print("국어 : ",s.kor)  # 80
print("합계 : ",s.total) # 240
s.kor = 100
print("국어 : ",s.kor) # 100
s.total_f()
s.avg_f()
print("합계 : ",s.total) # 260
print("평균 : ",s.avg) # 


# -------------------------------
# 클래스 선언
# class Student:
#     pass
# s = Student()   # 객체선언
# s.stuno = 10101 # 변수추가
# print(s.stuno) # 변수출력

# #--------------------------------
# stuno = 10101
# print(stuno)