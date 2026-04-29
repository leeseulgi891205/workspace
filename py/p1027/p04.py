# 연산자 - 산술연산자(+, -, *, /, %)
# 비교연산자 - >,<,==,!=,>=,<=
# and - 두개모두 true 일때 true, 나머지 false
# or - 두개중 하나만 true 여도 true, 둘다 false 일때 false
# or - 두개 모두 false 일때 false, 나머지 true

print(10, "+",5, "=", 10+5)
print(2025+"년",10,"월",27,일)
print("2025 년 10월 27일")

print(10,"+",5,"=",10+5)

print(num + num2)
print(int(num)+int(num2))
print(num "+", num2, "=", int(num?)+int(num2))
print("%s + %s \%d" % (num, num2, int(num)+int(num2)))

# 앞쪽 문자열에 % 뒤의 변수값을 할당하는 방식
# 숫자-정수 %d (자리수 지정, 빈공백에 0채우기 가능)
# 숫자 실수 %f (자리수 지정, 소수점 제한까지 가능)
# 문자열 %s