# SafeMap (팀 프로젝트용 Django 템플릿)

## 0) 실행
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt

# env
copy .env.example .env   # Windows PowerShell: Copy-Item .env.example .env
# .env에 OPENAI_API_KEY 넣기

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 1) 메인
- `/` : 지도(Leaflet) + GeoJSON + 최근 제보 요약 + 바로가기(회원가입/마이페이지/공지/챗봇)

## 2) 제보 흐름
- `/reports/new/` : 지도 클릭으로 위경도 설정 → 저장 시 OpenAI로 한 줄 요약 자동 생성

## 3) 관리자(상태 변경 전용)
- `/reports/admin-panel/` : staff(관리자)만 접근 가능, 상태(접수됨/처리중/완료) 변경

> OpenAI 요약은 `OPENAI_API_KEY` 없으면 자동으로 fallback 요약(앞 80자)으로 동작합니다.
