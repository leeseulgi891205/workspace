# 세트 - 키만 있음. 키 중복불가
# 세트를 하면 중복이 제거 됨.
set1 = {1,1,2,3,4,2,5,4,4,4,1}
print(set(set1))

a_list = [1,2,3,1,15,6,7,3]
print(set(a_list))

names = ['홍길동','유관순','이순신','홍길동','홍길동','유관순'] # 중복을 제거해서 알려줌.
nset = set(names) # 변수에 저장해도 무방
print(nset)
print(set(names))
