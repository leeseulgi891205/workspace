# return문 : 함수를 호출한 곳으로 값을 전달할때 사용.
def cal(a,b): # a,b = int,int #매개변수는 꼭 타입을 맞춰서 전달해야함.
    return(a+b)        # 함수끝을 만나면 함수가 종료됨.
    #eturn a+b # a+b 결과값을 함수 호출한 곳으로 전달.
    # return     # return을 만나면 함수가 종료됨.


num1 = cal(10,5)
num2 = cal(2,7)
num3 = cal(3,5)
num3 = cal("3",5) #string + int 오류 타입이 다름


# 3개의 계산 더하기 빼기를 구하시오.



sum = cal(12321321321310,5123213213213)
print(num1+num2-num3)
print(num1+num2+num3)
