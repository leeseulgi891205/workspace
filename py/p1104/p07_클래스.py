# 클래스
# 클래스 내 변수,함수를 사용하려면, 무조건 객체선언을 해야 사용할수 있음.
# 객체선언 : 참조변수 = 클래스명
class Car:
        
    ## 생성자 : 객체선언시 값을 바로 할당할수 있도록 해줌.
    def __init__(self,color,speed):
        self.color = color  # self.변수명 시 없으면 클래스에 변수 추가해 줌.
        self.speed = speed
        self.tire = 4       # 변수가 없으면 자동생성
    
    # 생성자 생략
    # 클래스내 함수(self) : self는 함수밖에 변수를 찾아서 변경하기 위해 사용
    def upSpeed(self,num):
        # 함수내 변수를 선택
        self.speed += num
    
    def downSpeed(self,num):
        self.speed -= num  

# 1. 객체선언후 값지정 
# c1 = Car() # 객체선언
# c1.color = '파랑'  # 변수값지정
# c1.speed = 100    # 변수값지정
# print(c1.color)
# print(c1.speed)
 
# 2. 생성자를 통해 값지정 - 생성자를 사용해서 프로그램을 함.
# c2 = Car('파랑',100)  # 생성자의 매개변수 개수를 맞춰야 함.
# print(c2.color)
# print(c2.speed) 
# c2.door = 5  # 클래스에 변수가 없으면 클래스에 자동으로 추가 됨
# print(c2.door)
 
        
# c1 = Car()     # 객체선언 - 변수,함수사용
# # 사용방법 - 참조변수.변수명
# # 함수 - 참조변수.함수명
# print(c1.speed)
# c1.upSpeed(10) # 클래스 내 함수 호출 - 참조변수.함수명()
# print(c1.speed)

# # 속도 50으로 증가, 속도 30 감소, 속도 100
# # 속도를 출력하시오.
# # 색상 => 파랑 변경하시오.
# c1.upSpeed(50)
# c1.downSpeed(30)
# c1.upSpeed(100)
# c1.speed = -100 
# print(c1.speed)
# c1.color = '파랑'
# print(c1.color)