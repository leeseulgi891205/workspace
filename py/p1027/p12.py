# 년도 가져오기

import datetime

now = datetime.datetime.now()
year = now.year

# 주민번호를 입력받아, 나이를 출력하시오.
# 990101-1111111
# 000101-3111111

jumin = "070101-1111111" # 문자열
a1 = jumin[7] #a1 타입 - 문자열
num = int(a1) #문자열 -> 정수타입변경

# 1900년대생인지, 2000년대생인지 확인하시오.
# 조건문
if num == 1 or num == 2:
    year1 = jumin[:2] #문자열
    y_num =int(year1) #문자열 -> 정수타입변경
    print(2025 - (1900+num))
else:
    year1 = jumin[:2] #문자열
    y_num = int(year1) #문자열 -> 정수타입변경
    print(2025 - (2000+y_num))
    
if num==1 or num==2:
    





jumin = input("주민등록번호를 입력하세요 (990101-1234567): ")

# 입력 검증
if len(jumin) != 14 or jumin[6] != "-":
    print("올바른 형식이 아닙니다. (990101-1234567)")
else:
    birth = jumin[:6]
    gender_code = jumin[7]

    year = int(birth[:2])
    month = int(birth[2:4])
    day = int(birth[4:6])

print(f"출생일: {year}년 {month}월 {day}일")
print(f"현재 나이: {age}")