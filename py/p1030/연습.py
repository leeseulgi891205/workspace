# -----------------------------
# [AI 도우미 프로그램 v1.0]
# -----------------------------

import random
import datetime

# AI 응답 데이터베이스
greetings = [
    "안녕하세요! 저는 AI 도우미입니다! 😊",
    "반가워요! 무엇을 도와드릴까요? 🤖",
    "안녕! 오늘도 좋은 하루 보내세요! ✨",
    "어서오세요! AI 도우미가 준비되었습니다! 🚀"
]

weather_responses = [
    "오늘 날씨는 맑고 화창할 것 같아요! ☀️",
    "구름이 조금 있지만 괜찮은 날씨예요! ⛅",
    "비가 올 수도 있으니 우산을 챙기세요! 🌧️",
    "바람이 선선하고 좋은 날씨네요! 🍃"
]

motivational_quotes = [
    "포기하지 마세요! 당신은 할 수 있어요! 💪",
    "오늘도 최선을 다하는 당신이 멋져요! ⭐",
    "작은 노력들이 모여 큰 성과를 만듭니다! 🌟",
    "실패는 성공의 어머니입니다! 계속 도전하세요! 🔥",
    "당신의 꿈을 향해 한 걸음씩 나아가세요! 🎯"
]

jokes = [
    "프로그래머가 바에 간다면? 404 - Bar not found! 😄",
    "컴퓨터가 감기에 걸리면? 바이러스에 감염됐다고 해요! 🤧",
    "AI가 다이어트를 한다면? 데이터를 압축해요! 📦",
    "파이썬이 왜 인기가 많을까요? 간단하고 뱀같이 유연하거든요! 🐍"
]

advice_database = {
    "공부": [
        "조금씩이라도 꾸준히 하는 것이 중요해요! 📚",
        "복습을 잊지 마세요. 반복학습이 핵심입니다! 🔄",
        "집중할 수 있는 환경을 만들어보세요! 🎯"
    ],
    "운동": [
        "매일 30분씩 가벼운 운동부터 시작해보세요! 🏃‍♂️",
        "스트레칭으로 몸을 풀어주는 것도 중요해요! 🧘‍♀️",
        "친구와 함께 운동하면 더 재미있어요! 👫"
    ],
    "건강": [
        "충분한 수면이 가장 중요합니다! 😴",
        "물을 많이 마시고 규칙적인 식사를 하세요! 💧",
        "스트레스 관리도 건강의 핵심이에요! 🧠"
    ]
}

# 사용자 정보 저장
user_data = {}

# -----------------------------
# AI 기능 함수들
# -----------------------------

def ai_greeting():
    """AI 인사말"""
    print(random.choice(greetings))
    current_time = datetime.datetime.now()
    hour = current_time.hour
    
    if 6 <= hour < 12:
        print("좋은 아침이에요! 🌅")
    elif 12 <= hour < 18:
        print("좋은 오후예요! ☀️")
    elif 18 <= hour < 22:
        print("좋은 저녁이에요! 🌆")
    else:
        print("늦은 시간이네요. 일찍 주무세요! 🌙")

def ai_chatbot():
    """AI 챗봇 기능"""
    print("\n🤖 AI 챗봇과 대화하기")
    print("(종료하려면 '종료' 또는 'quit'를 입력하세요)")
    print("-" * 40)
    
    while True:
        user_input = input("당신: ").strip().lower()
        
        if user_input in ['종료', 'quit', '그만', '끝']:
            print("AI: 대화해주셔서 감사했어요! 또 만나요! 👋")
            break
        
        # 키워드 기반 응답
        if any(word in user_input for word in ['안녕', '하이', '헬로']):
            print("AI:", random.choice(greetings))
        
        elif any(word in user_input for word in ['날씨', '기상', '비', '맑음']):
            print("AI:", random.choice(weather_responses))
        
        elif any(word in user_input for word in ['힘들', '우울', '슬프', '스트레스']):
            print("AI:", random.choice(motivational_quotes))
        
        elif any(word in user_input for word in ['농담', '웃긴', '재미있는', '유머']):
            print("AI:", random.choice(jokes))
        
        elif any(word in user_input for word in ['공부', '학습', '시험']):
            print("AI:", random.choice(advice_database["공부"]))
        
        elif any(word in user_input for word in ['운동', '헬스', '다이어트']):
            print("AI:", random.choice(advice_database["운동"]))
        
        elif any(word in user_input for word in ['건강', '몸', '피로']):
            print("AI:", random.choice(advice_database["건강"]))
        
        elif any(word in user_input for word in ['이름', '누구', '소개']):
            print("AI: 저는 파이썬으로 만들어진 AI 도우미예요! 🤖")
        
        elif any(word in user_input for word in ['시간', '몇시', '언제']):
            now = datetime.datetime.now()
            print(f"AI: 지금 시간은 {now.strftime('%Y년 %m월 %d일 %H시 %M분')}이에요! ⏰")
        
        else:
            responses = [
                "흥미로운 말씀이네요! 더 자세히 말씀해주세요! 🤔",
                "아직 그에 대해서는 잘 모르겠어요. 다른 주제는 어떠세요? 😅",
                "좋은 생각이네요! 더 이야기해볼까요? 💭",
                "그렇군요! 다른 것도 궁금한 게 있나요? 🧐"
            ]
            print("AI:", random.choice(responses))

def ai_fortune_teller():
    """AI 운세 보기"""
    print("\n🔮 AI 운세 보기")
    print("-" * 40)
    
    name = input("이름을 입력하세요: ")
    
    fortunes = [
        f"{name}님, 오늘은 행운이 가득한 하루가 될 거예요! 🍀",
        f"{name}님, 새로운 기회가 찾아올 예정이에요! ✨",
        f"{name}님, 좋은 사람들과의 만남이 있을 거예요! 👥",
        f"{name}님, 창의적인 아이디어가 떠오를 거예요! 💡",
        f"{name}님, 건강에 특히 신경 쓰시는 게 좋겠어요! 💪"
    ]
    
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_color = random.choice(["빨간색", "파란색", "노란색", "초록색", "보라색", "주황색"])
    
    print(f"\n🎯 {name}님의 오늘 운세:")
    print(random.choice(fortunes))
    print(f"🎲 행운의 숫자: {', '.join(map(str, sorted(lucky_numbers)))}")
    print(f"🌈 행운의 색깔: {lucky_color}")

def ai_quiz_game():
    """AI 퀴즈 게임"""
    print("\n🧠 AI 퀴즈 게임")
    print("-" * 40)
    
    quiz_data = [
        {"question": "파이썬의 아버지로 불리는 사람은?", "answer": "귀도 반 로섬", "choices": ["귀도 반 로섬", "스티브 잡스", "빌 게이츠", "마크 저커버그"]},
        {"question": "1 + 1은?", "answer": "2", "choices": ["1", "2", "3", "4"]},
        {"question": "대한민국의 수도는?", "answer": "서울", "choices": ["부산", "서울", "대구", "인천"]},
        {"question": "AI의 줄임말은?", "answer": "인공지능", "choices": ["인공지능", "자동차", "컴퓨터", "로봇"]},
        {"question": "파이썬에서 주석을 나타내는 기호는?", "answer": "#", "choices": ["//", "#", "/*", "--"]}
    ]
    
    score = 0
    total_questions = len(quiz_data)
    
    for i, quiz in enumerate(quiz_data, 1):
        print(f"\n📝 문제 {i}: {quiz['question']}")
        for j, choice in enumerate(quiz['choices'], 1):
            print(f"{j}. {choice}")
        
        try:
            user_choice = int(input("정답 번호를 선택하세요 (1-4): "))
            if 1 <= user_choice <= 4:
                selected_answer = quiz['choices'][user_choice - 1]
                if selected_answer == quiz['answer']:
                    print("✅ 정답입니다!")
                    score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 '{quiz['answer']}'입니다.")
            else:
                print("❌ 1-4 사이의 숫자를 입력하세요.")
        except ValueError:
            print("❌ 숫자만 입력하세요.")
    
    print(f"\n🎉 퀴즈 완료! 점수: {score}/{total_questions}")
    if score == total_questions:
        print("🏆 완벽합니다! 천재시네요!")
    elif score >= total_questions * 0.8:
        print("👏 훌륭해요! 거의 다 맞혔네요!")
    elif score >= total_questions * 0.6:
        print("👍 좋아요! 평균 이상이에요!")
    else:
        print("💪 다음엔 더 잘할 수 있을 거예요!")

def ai_calculator():
    """AI 계산기"""
    print("\n🧮 AI 계산기")
    print("-" * 40)
    
    while True:
        print("\n계산 방법:")
        print("1. 더하기 (+)")
        print("2. 빼기 (-)")
        print("3. 곱하기 (*)")
        print("4. 나누기 (/)")
        print("5. 거듭제곱 (**)")
        print("0. 돌아가기")
        
        try:
            choice = int(input("선택하세요: "))
            
            if choice == 0:
                break
            elif 1 <= choice <= 5:
                num1 = float(input("첫 번째 숫자: "))
                num2 = float(input("두 번째 숫자: "))
                
                if choice == 1:
                    result = num1 + num2
                    print(f"🔢 {num1} + {num2} = {result}")
                elif choice == 2:
                    result = num1 - num2
                    print(f"🔢 {num1} - {num2} = {result}")
                elif choice == 3:
                    result = num1 * num2
                    print(f"🔢 {num1} × {num2} = {result}")
                elif choice == 4:
                    if num2 != 0:
                        result = num1 / num2
                        print(f"🔢 {num1} ÷ {num2} = {result}")
                    else:
                        print("❌ 0으로 나눌 수 없습니다!")
                elif choice == 5:
                    result = num1 ** num2
                    print(f"🔢 {num1} ^ {num2} = {result}")
            else:
                print("❌ 올바른 번호를 선택하세요.")
        except ValueError:
            print("❌ 숫자만 입력하세요.")

def ai_memory_game():
    """AI 기억력 게임"""
    print("\n🧩 AI 기억력 게임")
    print("-" * 40)
    print("숫자 순서를 기억하세요!")
    
    level = 1
    max_level = 5
    
    while level <= max_level:
        print(f"\n🎯 레벨 {level}")
        
        # 랜덤 숫자 시퀀스 생성
        sequence = [random.randint(1, 9) for _ in range(level + 2)]
        
        # 시퀀스 보여주기
        print("기억하세요:", ' → '.join(map(str, sequence)))
        
        # 잠시 대기
        import time
        time.sleep(2 + level * 0.5)
        
        # 화면 지우기 효과
        print("\n" * 10)
        print("이제 순서대로 입력하세요!")
        
        # 사용자 입력 받기
        user_sequence = []
        for i in range(len(sequence)):
            try:
                num = int(input(f"{i+1}번째 숫자: "))
                user_sequence.append(num)
            except ValueError:
                print("❌ 숫자만 입력하세요.")
                break
        
        # 정답 확인
        if user_sequence == sequence:
            print("✅ 정답입니다! 다음 레벨로!")
            level += 1
        else:
            print(f"❌ 틀렸습니다. 정답: {' → '.join(map(str, sequence))}")
            break
    
    if level > max_level:
        print("🏆 모든 레벨을 클리어했습니다! 기억력 천재!")
    else:
        print(f"🎮 게임 종료! 레벨 {level-1}까지 클리어!")

def user_profile():
    """사용자 프로필 관리"""
    global user_data
    
    print("\n👤 사용자 프로필")
    print("-" * 40)
    
    if not user_data:
        print("처음 오셨네요! 간단한 정보를 입력해주세요.")
        name = input("이름: ")
        age = input("나이: ")
        hobby = input("취미: ")
        
        user_data = {
            "name": name,
            "age": age,
            "hobby": hobby,
            "visit_count": 1
        }
        print(f"✅ {name}님, 환영합니다!")
    else:
        user_data["visit_count"] += 1
        print(f"👋 {user_data['name']}님, 다시 오셨네요!")
        print(f"📊 방문 횟수: {user_data['visit_count']}번")
        print(f"🎂 나이: {user_data['age']}세")
        print(f"🎯 취미: {user_data['hobby']}")

# -----------------------------
# 메인 프로그램
# -----------------------------

def main():
    """메인 프로그램"""
    ai_greeting()
    
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "🤖 AI 도우미 프로그램")
        print("=" * 50)
        print("1. 🗣️  AI 챗봇과 대화하기")
        print("2. 🔮 AI 운세 보기")
        print("3. 🧠 AI 퀴즈 게임")
        print("4. 🧮 AI 계산기")
        print("5. 🧩 AI 기억력 게임")
        print("6. 👤 사용자 프로필")
        print("7. 😄 랜덤 농담")
        print("8. 💪 동기부여 명언")
        print("0. 👋 프로그램 종료")
        print("=" * 50)
        
        try:
            choice = int(input("원하는 메뉴를 선택하세요 ▶ "))
        except ValueError:
            print("❌ 숫자만 입력하세요.")
            continue
        
        if choice == 1:
            ai_chatbot()
        elif choice == 2:
            ai_fortune_teller()
        elif choice == 3:
            ai_quiz_game()
        elif choice == 4:
            ai_calculator()
        elif choice == 5:
            ai_memory_game()
        elif choice == 6:
            user_profile()
        elif choice == 7:
            print("\n😄", random.choice(jokes))
        elif choice == 8:
            print("\n💪", random.choice(motivational_quotes))
        elif choice == 0:
            if user_data:
                print(f"👋 {user_data['name']}님, 이용해주셔서 감사합니다!")
            else:
                print("👋 이용해주셔서 감사합니다!")
            print("🤖 AI 도우미가 항상 응원할게요!")
            break
        else:
            print("❌ 올바른 메뉴 번호를 선택하세요.")
        
        input("\n⏸️  계속하려면 Enter를 누르세요...")

# 프로그램 시작
if __name__ == "__main__":
    main()