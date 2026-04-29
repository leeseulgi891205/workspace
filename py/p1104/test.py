import stuFunc
while True:
    stuFunc.screen_print()
    choice = int(input("원하는 번호를 입력하세요.>> "))

    if choice == 1:
        stuFunc.stu_input()
    elif choice == 2:
        stuFunc.stu_print()  
    elif choice == 3:
        stuFunc.stu_modify() 
    elif choice == 4:
        stuFunc.stu_delete()
    elif choice == 5:
        