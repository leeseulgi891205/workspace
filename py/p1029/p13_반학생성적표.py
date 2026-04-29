# while문으로 학생성적표 만들기.
# 1. 학생성적출력
# 2. 학생성적출력
# 3. 학생성적평균값 출력
# 4. 이름, 사회, 체육 ,과학, 점수 출력
# 5. 3명의 학생성적 출력

print("\n" + "="*50)
print("=== 학생 성적표 프로그램 ===")
print("="*50)

# 학생 정보를 저장할 리스트
students = []
count = 0  # 입력받은 학생 수

# while문으로 3명의 학생 성적 입력받기
while count < 3:
    print(f"\n{count + 1}번째 학생 정보를 입력하세요:")
    
    # 1. 학생 정보 입력
    name = input("이름: ")
    social = int(input("사회 점수: "))
    pe = int(input("체육 점수: "))
    science = int(input("과학 점수: "))
    
    # 2. 평균 계산
    total = social + int + science
    average = total / 3
    
    # 3. 학생 정보를 딕셔너리로 저장
    student = {
        'name': name,
        'social': social,
        'pe': pe,
        'science': science,
        'total': total,
        'average': average
    }
    
    students.append(student)
    count += 1

# 4. 전체 학생 성적 출력
print("\n" + "="*50)
print("=== 3명의 학생 성적표 === ")
print("="*50)
print("이름\t사회\t체육\t과학\t총점\t평균")
print("-" * 50)

student_num = 0
while student_num < len(students):
    s = students[student_num]
    print(f"{s['name']}\t{s['social']}\t{s['pe']}\t{s['science']}\t{s['total']}\t{s['average']:.1f}")
    student_num += 1

# 5. 전체 평균 계산 및 출력
total_average = 0
i = 0
while i < len(students):
    total_average += students[i]['average']
    i += 1

class_average = total_average / len(students)

print("-" * 50)
print(f"반 평균: {class_average:.1f}점")
print("="*50)
print("학생성적표 프로그램이 종료되었습니다.")