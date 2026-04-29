
; # 20문제 중 랜덤으로 5문제 선택
; quiz_keys = random.sample(list(english.keys()), 5)

; count = 0
; results = []

; print("영어 맞추기 퀴즈! 🌟 총 5문제입니다.\n")

; for idx, k in enumerate(quiz_keys, start=1):
;     print(f"{idx}. {k} 은(는) 영어로 뭘까요?")
;     answer = input(">> ")
    
;     # 대소문자 구분 없이 정답 확인
;     if answer.lower() == english[k].lower():
;         print("정답! 🎉\n")
;         count += 1
;         results.append("정답")
;     else:
;         print(f"틀렸습니다. 정답은 '{english[k]}'입니다.\n")
;         results.append("오답")

; # 문제별 결과 출력
; for i, res in enumerate(results, start=1):
;     print(f"{i}. {res}")

; print(f"\n총 {count}개 맞췄습니다. / 총 5개")