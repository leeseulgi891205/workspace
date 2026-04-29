




# for 변수 in 범위:
# pass = 빈공백 : for, if 한줄이라도 코드가 없으면 에러가 나기 때문에 pass쓴다.
# break = 반복문 즉시 종료
# continue = 1회 반복문을 제외시켜줌

# for i in range(10):
#     pass # 아무일도 일어나지 않음 - 빈공백
#     print("프로그램 종료")
#     break # 반복문을 즉시 종료

# for i in range(10):
#     if i%2 == 0:
#         print("프로그램 종료")
#         continue # 1회만 제외


# for i in range(2,10): # 8
#     for j in range(1,10): # 9
#         print("숫자: ", j) # 1-72
#         print("-"*50)

# for i in range(2,10): # 8
#     print(i)
#     for j in range(1,10): # 9
# print(j)

# for i in range(2,10): # 8번 출력 - 2,3,4,5,6,7,8,9
#     print(i)
    
# for i in range(8):
#     print(i)
    
# # 5,21까지 출력하시오
# for i in range(5,22):
#     print(i)
    
# # 1,10까지 출력하시오
# for i in range(1,11):
#     print(i)
    
# # 0,9까지 출력하고 홀수만 출력하시오.
# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i)


# 구구단을 출력하시오. #########################중요############################
# for i in range(2,10):
#     if i%2 == 1:
#         continue
#     for j in range(1,10):
#         print("[{}단]".format(i))
#         if i%2 == 1:
#             continue
#         print("{} x {} = {}".format(i,j,i*j))
#     print()
    

# names = ['홍길동','유관순','이순신','김구','강감찬']
# # for 변수 in 범위 : -> range(길이), list,문자열,딕셔너리,듀플

# for name in names:
#     print(name)         # 1.홍길동 2.유관순 3.이순신 4.김구 5.강감찬
    
    
# for i in enumerate(names): # index번호리턴, 값도 리턴
#     print(i[0], [1])     # 0.홍길동 1.유관순 2.이순신 3.김구 4.강감찬
    

# for i, name in enumerate(names):
#     print("{}: {}".format(i+1, name))
    
# n_list = [
#     [1, '홍길동'],
#     [2, '유관순'],
#     [3, '이순신'],
#     [4, '김구'],
#     [5, '강감찬']
# ]
# for ns in n_list: #[1, '홍길동'], [2, '유관순'],[3, '이순신']
#     for n in ns:
#         print(n, end="  ")
#     print()
    
a_list = [0]
# for문을 사용해서 0을 10개 들어가는 리스트를 만드시오.
# append() - 함수 : 리스트에 추가
for i in range(10):
    a_list.append('0')
print(a_list)

a_list = list('0'*10)
print(a_list)

a_list = ['0' for i in range(10)] # 한줄 for문
print(a_list)

a_list = [2*i+i for i in range(1,10)]
print(a_list)