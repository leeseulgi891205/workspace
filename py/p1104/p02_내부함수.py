# lambda() 함수 - 함수를 한줄로 간단히 만든 것

# 함수선언,함수정의
# def add(a,b):
#     result = a + b
#     return result
# # 함수호출
# print(add(10,20))

# 함수축약 lambda() # def선언하는 것과 같음.
# lambda 매개변수 : 함수수식
# add(값,값) 함수호출
# lambda 간단한 함수만 가능
# 복잡한 함수는 기본함수를 사용해야 함.
# add = lambda a,b : a+b
# print(add(10,20))

# cal = lambda a:a**2
# print(cal(10))

# result = lambda a:a%2
# print(result(3))
   
# map함수
# 결과값리스트 = map(함수,리스트)
# 결과값리스트 - map타입 객체 -> list타입으로 변경

# # my_list = ['0']*10
# print(my_list)
# def cal(a):
#     return a%2
# map(함수,리스트)
# m_list = list(map(cal,my_list))
# print(m_list)

# 람다식함수 - 함수축약 / 변수 = lambda 매개변수: 수식
# map함수  - 여러개를 함수적용시킬때 사용 / 리스트 = map(함수,리스트)
my_list = [1,2,3,4,5]
m_list = list(map(lambda a:"{}원".format(a*1425),my_list))
print(m_list)
m_list = list(map(lambda a:a*10,my_list))
print(m_list)
my_list = ['1','2','3','4','5']
m_list = list(map(lambda a:int(a),my_list))
print(m_list)





    



# 내부함수 - 함수내에 함수
# def outFunc(a,b):
#     def inFunc(n1,n2):
#         return n1+n2
#     return inFunc(a,b)

# print(outFunc(10,20))

# def outFunc(a,b):
#     result = a+b
#     return result

# def inFunc(n1,n2):
#     return n1+n2