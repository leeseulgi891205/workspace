# -----------------------------
# [학생 성적 프로그램 with 로그인 v2.0]
# -----------------------------

# 사용자 계정 정보를 저장하는 딕셔너리
# 구조: {아이디: [패스워드, 이름, 이메일]}
user_accounts = {
    "admin": ["1234", "관리자", "admin@school.com"],
    "teacher1": ["5678", "김선생", "kim@school.com"],
    "student1": ["abcd", "홍길동", "hong@school.com"]
}

# 학생 성적 데이터를 저장하는 2차원 리스트
stu_list = [
    [10101, '홍길동', 80, 90, 80, 250, 83.33],
    [10102, '유관순', 90, 90, 90, 270, 90.00],
    [10103, '이순신', 100, 100, 100, 300, 100.00]
]

stu_count = 10104  # 새로 입력할 학생의 번호
titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균']

# 현재 로그인한 사용자 정보
current_user = None
is_logged_in = False

# -----------------------------
# 로그인 관련 함수들
# -----------------------------

def login_system():
    """로그인 시스템 메인 메뉴"""
    global current_user, is_logged_in
    
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "🔐 로그인 시스템")
        print("=" * 50)
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 아이디 찾기")
        print("4. 비밀번호 찾기")
        print("5. 계정 정보 수정")
        print("0. 프로그램 종료")
        print("=" * 50)
        
        try:
            choice = int(input("메뉴를 선택하세요 ▶ "))
        except ValueError:
            print("❌ 숫자만 입력하세요.")
            continue
        
        if choice == 1:
            if login():
                is_logged_in = True
                return True  # 로그인 성공시 성적 프로그램으로 이동
        elif choice == 2:
            register()
        elif choice == 3:
            find_id()
        elif choice == 4:
            find_password()
        elif choice == 5:
            modify_account()
        elif choice == 0:
            print("👋 프로그램을 종료합니다.")
            return False
        else:
            print("❌ 올바른 메뉴 번호를 선택하세요.")

def login():
    """로그인 기능"""
    global current_user
    
    print("\n📱 로그인")
    print("-" * 30)
    
    user_id = input("아이디를 입력하세요 ▶ ")
    password = input("비밀번호를 입력하세요 ▶ ")
    
    # 아이디가 존재하는지 확인
    if user_id in user_accounts:
        # 비밀번호가 맞는지 확인
        if user_accounts[user_id][0] == password:
            current_user = user_id
            print(f"✅ {user_accounts[user_id][1]}님, 환영합니다!")
            return True
        else:
            print("❌ 비밀번호가 틀렸습니다.")
            return False
    else:
        print("❌ 존재하지 않는 아이디입니다.")
        return False

def register():
    """회원가입 기능"""
    print("\n📝 회원가입")
    print("-" * 30)
    
    # 아이디 입력 및 중복 확인
    while True:
        user_id = input("사용할 아이디를 입력하세요 ▶ ")
        if user_id in user_accounts:
            print("❌ 이미 존재하는 아이디입니다. 다른 아이디를 입력하세요.")
        elif len(user_id) < 3:
            print("❌ 아이디는 3글자 이상이어야 합니다.")
        else:
            break
    
    # 비밀번호 입력 및 확인
    while True:
        password = input("비밀번호를 입력하세요 ▶ ")
        if len(password) < 4:
            print("❌ 비밀번호는 4글자 이상이어야 합니다.")
            continue
        
        password_confirm = input("비밀번호를 다시 입력하세요 ▶ ")
        if password == password_confirm:
            break
        else:
            print("❌ 비밀번호가 일치하지 않습니다.")
    
    name = input("이름을 입력하세요 ▶ ")
    email = input("이메일을 입력하세요 ▶ ")
    
    # 계정 정보 저장
    user_accounts[user_id] = [password, name, email]
    print(f"✅ {name}님의 계정이 성공적으로 생성되었습니다!")

def find_id():
    """아이디 찾기 기능"""
    print("\n🔍 아이디 찾기")
    print("-" * 30)
    
    name = input("이름을 입력하세요 ▶ ")
    email = input("이메일을 입력하세요 ▶ ")
    
    found_ids = []
    for user_id, info in user_accounts.items():
        if info[1] == name and info[2] == email:
            found_ids.append(user_id)
    
    if found_ids:
        print("✅ 찾은 아이디:")
        for user_id in found_ids:
            print(f"   - {user_id}")
    else:
        print("❌ 일치하는 계정을 찾을 수 없습니다.")

def find_password():
    """비밀번호 찾기 기능"""
    print("\n🔍 비밀번호 찾기")
    print("-" * 30)
    
    user_id = input("아이디를 입력하세요 ▶ ")
    
    if user_id in user_accounts:
        name = input("이름을 입력하세요 ▶ ")
        email = input("이메일을 입력하세요 ▶ ")
        
        if user_accounts[user_id][1] == name and user_accounts[user_id][2] == email:
            print(f"✅ 비밀번호: {user_accounts[user_id][0]}")
        else:
            print("❌ 입력한 정보가 일치하지 않습니다.")
    else:
        print("❌ 존재하지 않는 아이디입니다.")

def modify_account():
    """계정 정보 수정 기능"""
    print("\n✏️ 계정 정보 수정")
    print("-" * 30)
    
    user_id = input("아이디를 입력하세요 ▶ ")
    
    if user_id not in user_accounts:
        print("❌ 존재하지 않는 아이디입니다.")
        return
    
    current_password = input("현재 비밀번호를 입력하세요 ▶ ")
    
    if user_accounts[user_id][0] != current_password:
        print("❌ 비밀번호가 틀렸습니다.")
        return
    
    print("\n수정할 정보를 선택하세요:")
    print("1. 비밀번호 변경")
    print("2. 이름 변경")
    print("3. 이메일 변경")
    
    try:
        choice = int(input("선택 ▶ "))
    except ValueError:
        print("❌ 숫자만 입력하세요.")
        return
    
    if choice == 1:
        new_password = input("새 비밀번호를 입력하세요 ▶ ")
        if len(new_password) >= 4:
            user_accounts[user_id][0] = new_password
            print("✅ 비밀번호가 변경되었습니다.")
        else:
            print("❌ 비밀번호는 4글자 이상이어야 합니다.")
    elif choice == 2:
        new_name = input("새 이름을 입력하세요 ▶ ")
        user_accounts[user_id][1] = new_name
        print("✅ 이름이 변경되었습니다.")
    elif choice == 3:
        new_email = input("새 이메일을 입력하세요 ▶ ")
        user_accounts[user_id][2] = new_email
        print("✅ 이메일이 변경되었습니다.")
    else:
        print("❌ 올바른 선택이 아닙니다.")

# -----------------------------
# 학생 성적 프로그램 함수들
# -----------------------------

def student_management_system():
    """학생 성적 관리 시스템 메인"""
    global stu_count
    
    while True:
        print("\n" + "=" * 50)
        print(" " * 10 + f"📚 학생성적프로그램")
        print(f" " * 15 + f"사용자: {user_accounts[current_user][1]}님")
        print("=" * 50)
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("3. 학생성적수정")
        print("4. 학생성적삭제")
        print("5. 로그아웃")
        print("0. 프로그램종료")
        print("=" * 50)
        
        try:
            choice = int(input("원하는 번호를 선택하세요 ▶ "))
        except ValueError:
            print("❌ 올바른 숫자를 입력하세요.")
            continue
        
        if choice == 1:
            add_student()
        elif choice == 2:
            show_students()
        elif choice == 3:
            modify_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print(f"👋 {user_accounts[current_user][1]}님, 로그아웃되었습니다.")
            return False  # 로그인 화면으로 돌아가기
        elif choice == 0:
            print("👋 프로그램을 종료합니다.")
            return True   # 프로그램 완전 종료
        else:
            print("❌ 올바른 메뉴 번호를 선택하세요.")

def add_student():
    """학생 성적 입력"""
    global stu_count
    
    print("\n📝 [학생성적입력]")
    print("-" * 30)
    
    name = input(f"{stu_count}번 학생 이름을 입력하세요 ▶ ")
    
    try:
        kor = int(input("국어 점수를 입력하세요 ▶ "))
        eng = int(input("영어 점수를 입력하세요 ▶ "))
        math = int(input("수학 점수를 입력하세요 ▶ "))
    except ValueError:
        print("❌ 점수는 숫자만 입력하세요.")
        return
    
    total = kor + eng + math
    avg = total / 3
    
    stu_list.append([stu_count, name, kor, eng, math, total, avg])
    stu_count += 1
    print("✅ 성적 입력이 완료되었습니다.")

def show_students():
    """학생 성적 출력"""
    print("\n📊 [학생성적리스트]")
    print("=" * 60)
    print("{:<8}{:<8}{:<6}{:<6}{:<6}{:<6}{:<6}".format(*titles))
    print("=" * 60)
    
    for stus in stu_list:
        print("{:<8}{:<8}{:<6}{:<6}{:<6}{:<6.0f}{:<6.2f}".format(*stus))
    print("=" * 60)

def modify_student():
    """학생 성적 수정"""
    print("\n✏️ [학생성적수정]")
    print("-" * 30)
    
    if not stu_list:
        print("❌ 등록된 학생이 없습니다.")
        return
    
    for i, stu in enumerate(stu_list):
        print(f"[{i}] {stu[1]}")
    
    try:
        num = int(input("수정하려는 학생 번호를 입력하세요 ▶ "))
    except ValueError:
        print("❌ 올바른 숫자를 입력하세요.")
        return
    
    if num < 0 or num >= len(stu_list):
        print("❌ 올바른 학생 번호를 입력하세요.")
        return
    
    print(f"\n{stu_list[num][1]} 학생을 선택하였습니다.")
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    
    try:
        subject = int(input("수정할 과목을 선택하세요 ▶ "))
    except ValueError:
        print("❌ 올바른 숫자를 입력하세요.")
        return
    
    if subject < 1 or subject > 3:
        print("❌ 1, 2, 3 중에서 선택하세요.")
        return
    
    print(f"현재 {titles[subject+1]} 점수: {stu_list[num][subject+1]}")
    
    try:
        score = int(input(f"수정할 {titles[subject+1]} 점수를 입력하세요 ▶ "))
    except ValueError:
        print("❌ 점수는 숫자만 입력하세요.")
        return
    
    stu_list[num][subject+1] = score
    stu_list[num][5] = stu_list[num][2] + stu_list[num][3] + stu_list[num][4]
    stu_list[num][6] = stu_list[num][5] / 3
    print("✅ 성적 수정이 완료되었습니다.")

def delete_student():
    """학생 성적 삭제"""
    print("\n🗑️ [학생성적삭제]")
    print("-" * 30)
    
    if not stu_list:
        print("❌ 등록된 학생이 없습니다.")
        return
    
    for idx, stus in enumerate(stu_list):
        print(f"{idx+1}. {stus[0]} {stus[1]}")
    
    try:
        del_choice = int(input("삭제하려는 번호를 입력하세요 ▶ "))
    except ValueError:
        print("❌ 올바른 숫자를 입력하세요.")
        return
    
    if del_choice < 1 or del_choice > len(stu_list):
        print("❌ 올바른 학생 번호를 입력하세요.")
        return
    
    try:
        flag = int(input(f"{stu_list[del_choice-1][0]} {stu_list[del_choice-1][1]} 학생이 맞습니까? (1.예/2.아니오) ▶ "))
    except ValueError:
        print("❌ 1 또는 2를 입력하세요.")
        return
    
    if flag == 1:
        del stu_list[del_choice-1]
        print("✅ 삭제가 완료되었습니다.")
    else:
        print("❌ 삭제가 취소되었습니다.")

# -----------------------------
# 메인 프로그램 실행
# -----------------------------

def main():
    """메인 프로그램"""
    print("🎓 학생 성적 관리 시스템에 오신 것을 환영합니다!")
    
    while True:
        # 로그인 시스템 실행
        if login_system():
            # 로그인 성공시 성적 관리 시스템 실행
            if student_management_system():
                break  # 프로그램 완전 종료
        else:
            break  # 프로그램 완전 종료

# 프로그램 시작
if __name__ == "__main__":
    main()