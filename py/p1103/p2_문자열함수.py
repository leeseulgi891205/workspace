# 문자열 함수
# lower() 소문자로 변경
# uppre() 대문자로 변경
# swapcase() 대문자는 소문자로, 소문자는 대문자로 변경
# title() 각 단어의 첫글자만 대문자로 변경



# 문자열 찾기 방법
# count() - 해당되는 문자 개수를 출력시킴
# find() - 해당되는 문자의 위치를 출력시킴(없으면 -1 반환)
# index() - 해당되는 문자의 위치를 출력시킴(없으면 오류 발생
# rfind() - 오른쪽에서부터 해당되는 문자의 위치를 출력시킴(없으면 -1 반환)
# rindex() - 오른쪽에서부터 해당되는 문자의 위치를 출력시킴(없으면 오류 발생)
# starstwutn () - 해당 문자로 시작하는지 확인(True/False)
# endswith () - 해당 문자로 끝나는지 확인(True/False)

# 문자열 공백 제거
# strip() - 문자열 양쪽 공백 제거 (문자 사이 공백은 제거되지 않음.)
# rstrip() - 문자열 오른쪽 공백 제거
# lstrip() - 문자열 왼쪽 공백 제거
# replace() - 문자열 바꾸기(변경전 문자, 변경후 문자)

# split() - 문자열 분리(구분자 기준으로 나눔, 구분자 생략시 공백기준)
# 타입은 리스트로 분리 해줌.

# join() - 문자열 합치기(구분자 기준으로 합침)
# ss = "-"
# print(ss.join('파이썬'))

# map() - 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# map(function 함수부분의 리스트데이터)
# 리스트의 모든 원소를 함수에 적용한 결과를 map 객체로 반환

# isdigit() - 숫자여부 확인
# isalpha() - 문자여부 확인
# isalnum() - 문자+숫자 여부 확인
# islower() - 소문자 여부 확인
# isupper() - 대문자 여부 확인


# 국어 점수를 입력하세요.
while True:
    kor = input("국어 점수를 입력하세요.")
    if kor.isdigit(): # 입력된 값이 숫자로만 구성되어 있는지 확인
        print(int(kor))
        break
    else:
        print("숫자만 입력하세요. 다시 입력하세요")
print("숫자로 변경: ",int(kor))




# def multi(x):
#     return x * 2 
# a = [1,2,3] # 리스트 데이터
# b = list(map(multi,a)) # map타입에 리스트 형태로 변환
# print(a)
# print(b)






# a = ['100','90','80']
# print(map(int,a)) # map타입으로 출력
# b = list(map(int,a)) # map타입에 리스트 형태로 변환
# print(a)
# print(b)

# aa = [1,2,3]
# bb = list(map(lambda(),aa))
# print(aa)
# print(bb)

# a = ['1','2','3','4','5']
# a = ['100','90','80'] 
# b = []
# for i in a: 
#     b.append(int(i)) # 문자열을 정수로 변환하여 b리스트에 추가
    
# print(a)
# print(b)



# a = '1,홍길동,100,100,100,300,100,0'
# titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']

# print(sep:변수사이사이 모두 적용, end:마지막에 한번)

# print(*titles,sep="/",end='**') # sep='\t' 탭간격으로 출력 end='**' 마지막에 ** 출력





# a_list = a.split(',') # , 기준으로 분리
# print(*titles,sep='\t') # sep='\t' 탭간격으로 출력
# print("-"*50)
# print(*a_list,sep='\t')


# a_list = a.split(',') # , 기준으로 분리
# print(a_list[0]) # 0번째 홍길동 # 1번째 100 , 2번째 100 , 3번째 100 , 4번째 300

# b = '홍길동 유관순 이순신 김구'
# b_list = b.split(' ') # 공백 기준으로 분리
# print(b_list[1]) # ['홍길동', '유관순', '이순신', '김구']





# a = "홍길동은 키가 180cm 입니다. 홍길동은 몸무게 70kg, 홍길동은 사는 곳이 서울입니다."
# print(a.replace("홍길동","홍길자")) # 홍길동을 홍길자로 모두 변경






# ' ', ''
# a = "         a  b  c        "
# print(a.replace(' ',''))
# print(a.strip())

# input1 = input("아름을 입력하세요.>>").replace(' ','')
# if '홍길동' == input1:
#     print("맞습니다.",input1)
# else:
#     print("틀렸습니다.",input1)




# a = '112233333445'
# print(a.count('3')) # 3 - 5개 존재


# b = '프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그래밍)'
# print(b.find('파이썬')) # 왼쪽에서 파이썬 위치 검색 - 없을경우 -1 리턴
# print(b.rfind('파이썬')) # 오른쪽에서부터 파이썬 위치 검색
# print(b.index('파이썬')) # 왼쪽에서 파이썬 위치 검색, 없을때 에러
# print(b.rindex('파이썬')) # 오른쪽에서부터 파이썬 위치 검색, 없을때 에러
# print(b.startswith('파이썬'))
# c = "abc.xls"
# print(c.endswith('xsl')) 


# a = 'abc'
# # 대문자로 변경방법
# a_upper = ()

# b = 'aBBccDf'
# print(b.upper) 





# # 문자열
# # 문자열 슬라이싱

# a = "안녕하세요"
# # 하세를 출력하시오.
# print(a[2:4]) # 2부터 4직전까지
# print('안녕'*3) # 3번 반복
# print('안녕'+'하세요') # 문자열 연결