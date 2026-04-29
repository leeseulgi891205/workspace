#990101-1111111
#870101-2111111
# 1 - 남자 2 - 여자
#주민번호를 입력받아, 남자인지, 여자인지 출력하시오

jumin = input("주민등록번호를 입력하세요.:")

if len(jumin) != 14 or jumin[6] != "-":
    print("올바른 형식이 아닙니다. (예: 990101-1234567)")
else:
    gender_code = jumin[7]

    if gender_code in ["1", "3", "5", "7"]:
        print("남자입니다.")
    elif gender_code in ["2", "4", "6", "8"]:
        print("여자입니다.")
    else:
        print("잘못된 주민등록번호입니다.")



    

 

