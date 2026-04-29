# 맘스로그(MomsLog) 프로젝트 파일 구조

**프로젝트명:** 맘스로그 (MomsLog)  
**프레임워크:** Django 5.2.9  
**데이터베이스:** SQLite3  
**작성일:** 2026-01-13

---

## 📁 최상위 디렉토리 구조

```
mompjt(최종본절대수정금지)/
├── accounts/              # 계정 관리 앱
├── board/                 # 게시판 앱 (자유, 공지, 벼룩시장, 핫딜)
├── chat/                  # 채팅 앱
├── chatbot/               # 챗봇 앱
├── main/                  # 메인 페이지 앱
├── map/                   # 지도 앱
├── quests/                # 퀘스트 앱
├── recipes/               # 요리레시피 앱
├── mompjt/                # 프로젝트 설정 (settings.py, urls.py)
├── static/                # 정적 파일 (CSS, JS, 이미지)
├── staticfiles/           # 수집된 정적 파일
├── media/                 # 사용자 업로드 파일
├── templates/             # 전역 템플릿
├── manage.py              # Django 관리 명령어
└── db.sqlite3             # 데이터베이스 파일
```

---

## 📱 주요 앱 구조

### 1️⃣ **accounts/** - 회원 관리
```
accounts/
├── migrations/            # 데이터베이스 마이그레이션
├── templates/accounts/
│   ├── login/            # 로그인 페이지
│   ├── signup/           # 회원가입 페이지
│   └── mypage/           # 마이페이지 (프로필, 비밀번호 변경 등)
├── templatetags/         # 커스텀 템플릿 태그
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── forms.py              # 폼 클래스
├── models.py             # 데이터 모델 (UserProfile)
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수
└── __init__.py
```

**주요 기능:**
- 회원가입 / 로그인 / 로그아웃
- 프로필 관리
- 비밀번호 변경
- 계정 삭제

---

### 2️⃣ **board/** - 게시판 (가장 큰 앱)
```
board/
├── migrations/           # 데이터베이스 마이그레이션
├── management/
│   └── commands/        # 커스텀 관리 명령어
├── templates/board/
│   ├── free_list.html           # 자유게시판 목록
│   ├── free_detail.html         # 자유게시판 상세보기
│   ├── free_write.html          # 자유게시판 글쓰기
│   ├── notice_list.html         # 공지사항 목록
│   ├── notice_detail.html       # 공지사항 상세보기
│   ├── flea_list.html           # 벼룩시장 목록
│   ├── flea_detail.html         # 벼룩시장 상세보기
│   ├── flea_write.html          # 벼룩시장 상품 등록
│   ├── pet_list.html            # 반려동물 게시판 목록
│   ├── pet_detail.html          # 반려동물 게시판 상세보기
│   ├── parenting_list.html      # 육아정보 게시판 목록
│   ├── parenting_detail.html    # 육아정보 게시판 상세보기
│   ├── hotdeal_list.html        # 핫딜공유 게시판 목록
│   └── hotdeal_detail.html      # 핫딜공유 게시판 상세보기
├── templatetags/         # 커스텀 템플릿 태그
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── forms.py              # 폼 클래스
├── models.py             # 데이터 모델 (FreePost, Notice, FleaPost 등)
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수 (매우 큼 - 390줄 이상)
└── __init__.py
```

**게시판 종류:**
- 자유게시판 (FreePost)
- 공지사항 (Notice)
- 벼룩시장 (FleaPost) - 상품 판매
- 핫딜공유 (HotdealPost)
- 요리레시피 (recipes 앱)
- 반려동물 (PetPost)
- 육아정보 (ParentingPost)

---

### 3️⃣ **chat/** - 실시간 채팅
```
chat/
├── migrations/           # 데이터베이스 마이그레이션
├── management/
│   └── commands/        # 커스텀 관리 명령어
├── templates/chat/
│   └── chat_widget.html # 채팅 위젯 (448줄)
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── forms.py              # 폼 클래스
├── models.py             # 데이터 모델 (ChatRoom, ChatMessage)
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수
└── __init__.py
```

**주요 기능:**
- 채팅방 생성 / 조회
- 메시지 송수신 (AJAX)
- 채팅 기록 저장
- 입장 메시지 (sessionStorage 기반)

---

### 4️⃣ **recipes/** - 요리레시피 게시판
```
recipes/
├── migrations/           # 데이터베이스 마이그레이션
├── management/
│   └── commands/        # 커스텀 관리 명령어
├── templates/recipes/
│   ├── recipe_list.html      # 레시피 목록
│   ├── recipe_detail.html    # 레시피 상세보기
│   └── recipe_form.html      # 레시피 작성/수정
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── forms.py              # 폼 클래스
├── models.py             # 데이터 모델 (RecipePost, RecipeImage, RecipeComment)
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수 (390줄)
└── __init__.py
```

**주요 기능:**
- 레시피 게시글 작성 / 수정 / 삭제
- 이미지 업로드 (최대 10장)
- 댓글 기능

---

### 5️⃣ **quests/** - 일일 퀘스트
```
quests/
├── migrations/           # 데이터베이스 마이그레이션
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── context_processors.py # 템플릿 컨텍스트 프로세서
├── models.py             # DailyQuest 모델
├── services.py           # 비즈니스 로직
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수
└── __init__.py
```

**주요 기능:**
- 일일 퀘스트 생성 및 추적
- 사용자별 퀘스트 완료 여부 저장

---

### 6️⃣ **main/** - 메인 페이지
```
main/
├── migrations/           # 데이터베이스 마이그레이션
├── templates/main/
│   ├── index.html        # 홈페이지
│   └── search_result.html # 통합 검색 결과
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── models.py             # 데이터 모델
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수
└── __init__.py
```

**주요 기능:**
- 통합 검색 (모든 게시판 검색)
- 사이트 홈페이지

---

### 7️⃣ **chat/bot/** - 챗봇
```
chatbot/
├── migrations/           # 데이터베이스 마이그레이션
├── templates/chatbot/
│   └── chatbot_widget.html
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── models.py             # 데이터 모델
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수
└── __init__.py
```

---

### 8️⃣ **map/** - 지도
```
map/
├── migrations/           # 데이터베이스 마이그레이션
├── templates/map/
│   └── map.html
├── admin.py              # 관리자 페이지 설정
├── apps.py               # 앱 설정
├── models.py             # 데이터 모델
├── urls.py               # URL 라우팅
├── views.py              # 뷰 함수
└── __init__.py
```

---

## ⚙️ 프로젝트 설정 폴더

### mompjt/ - Django 프로젝트 설정
```
mompjt/
├── settings.py           # 프로젝트 설정
│   ├── DEBUG = True
│   ├── INSTALLED_APPS 리스트
│   ├── DATABASE 설정 (SQLite3)
│   ├── TEMPLATES 설정
│   └── STATIC_FILES 설정
├── urls.py               # 전체 URL 라우팅
├── asgi.py               # ASGI 설정 (배포용)
├── wsgi.py               # WSGI 설정 (배포용)
└── __init__.py
```

---

## 📂 정적 파일 (static/)

```
static/
├── css/                  # 스타일시트
│   ├── search_result.css
│   ├── board.css
│   └── ... (기타 CSS 파일)
├── js/                   # JavaScript 파일
│   ├── chat.js
│   ├── flea_write.js
│   └── ... (기타 JS 파일)
├── images/               # 이미지 파일
│   └── logo.png 등
└── videos/               # 비디오 파일
```

---

## 📥 미디어 파일 (media/)

사용자가 업로드한 파일들이 저장되는 폴더

```
media/
├── flea/                 # 벼룩시장 상품 이미지
├── recipes/              # 요리레시피 이미지
├── pet/                  # 반려동물 이미지
├── free_attachments/     # 자유게시판 첨부파일
├── parenting/            # 육아정보 이미지
├── pet_counsel/          # 펫 상담 파일
└── pet_health/           # 펫 건강 파일
```

---

## 🗄️ 데이터베이스 (db.sqlite3)

SQLite3 데이터베이스 파일  
**주요 테이블:**
- auth_user (Django 기본 사용자 테이블)
- accounts_userprofile (확장된 사용자 정보)
- board_freepost (자유게시판)
- board_notice (공지사항)
- board_fleapost (벼룩시장)
- board_petpost (반려동물 게시판)
- chat_chatroom (채팅방)
- chat_chatmessage (채팅 메시지)
- recipes_recipepost (레시피 게시글)
- quests_dailyquest (일일 퀘스트)

---

## 🔧 주요 수정 사항 (2026-01-13)

✅ **accounts/views.py**
- 로그인 실패 시 에러 메시지 표시
- 로그인 성공 시 성공 메시지 표시

✅ **board/templates/board/free_detail.html**
- 이전글/다음글 네비게이션 추가
- CSS 클래스 기반 스타일링

✅ **board/templates/board/flea_write.html**
- 이미지 최대 10장 업로드 지원
- MAX_FILES 상수 정의

✅ **main/templates/main/search_result.html**
- 자유게시판 검색 결과 URL 수정
- free_detail로 직접 이동

✅ **chat/templates/chat/chat_widget.html**
- sessionStorage 기반 입장 메시지
- 메시지 지속성 개선

✅ **quests/** 앱
- 데이터베이스 스키마 동기화
- context_processors.py 활성화

✅ **recipes/** 앱
- 새 폴더에서 덮어씌우기 (2026-01-13)

---

## 🚀 사용 방법

### 1. 프로젝트 실행
```bash
python manage.py runserver
```

### 2. 관리자 페이지
```
http://127.0.0.1:8000/admin/
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 정적 파일 수집
```bash
python manage.py collectstatic
```

---

## 📝 주요 URL 패턴

| URL | 설명 |
|-----|------|
| `/` | 홈페이지 |
| `/accounts/login/` | 로그인 |
| `/accounts/signup/` | 회원가입 |
| `/accounts/mypage/` | 마이페이지 |
| `/board/free/` | 자유게시판 |
| `/board/notice/` | 공지사항 |
| `/board/flea/` | 벼룩시장 |
| `/board/pet/` | 반려동물 게시판 |
| `/recipes/` | 요리레시피 |
| `/search/?q=키워드` | 통합 검색 |
| `/chat/` | 채팅 페이지 |

---

**마지막 업데이트:** 2026-01-13  
**상태:** ✅ 최종본 (수정 금지)
