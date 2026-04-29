# 파이썬은 여러개 리턴이 가능
# 리턴 형태 : 튜플, 리스트, 딕셔너리 등등
# 리스트 형태로 값을 리턴하면 여러개의 값을 리턴할수 있다.


#여러개 리턴

def cal():
    return 10,20,30 #파이썬만 가능한 튜플 리턴 방식.
a,b,c = cal()  # 튜플 언패킹
print(cal())  # 튜플로 넘어옴.
print(a,b,c)


# 리스트를 사용해서 여러개 리턴, 리턴값은 1개

def func():
    a_list = [10,20,30]
    return a_list

a_list = func()
print(a_list)