# p0205_06 프로젝트 - 게시판 기능 설정 가이드

## 1. 데이터베이스 테이블 생성

**파일**: `board_table_init.sql`

### Oracle SQL Developer 또는 SQL*Plus에서 실행:

```sql
-- 전체 스크립트 실행
@C:\workspace\JSP7\p0205_06\board_table_init.sql

-- 또는 개별 실행:

-- 테이블 생성
DROP TABLE board CASCADE CONSTRAINTS;
DROP SEQUENCE board_seq;

CREATE TABLE board (
    no          NUMBER          PRIMARY KEY,
    title       VARCHAR2(100)   NOT NULL,
    writer      VARCHAR2(20)    NOT NULL,
    writedate   DATE            DEFAULT SYSDATE,
    views       NUMBER          DEFAULT 0,
    content     CLOB            NOT NULL,
    pwd         VARCHAR2(20)    NOT NULL
);

-- 시퀀스 생성
CREATE SEQUENCE board_seq
    START WITH 1
    INCREMENT BY 1;

-- 샘플 데이터 삽입
INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, 'JSP 게시판 프로젝트', 'admin', SYSDATE, 5, 
'JSP와 Oracle을 이용한 게시판 프로젝트입니다.', '1234');

INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, '첫 번째 글입니다', 'user01', SYSDATE-1, 3, 
'안녕하세요. 이것은 첫 번째 게시글입니다.', '5678');

COMMIT;

-- 데이터 확인
SELECT * FROM board ORDER BY no DESC;
```

## 2. 프로젝트 구조

```
p0205_06/
├── src/main/java/com/java/www/
│   ├── Controller/
│   │   └── FController.java (메인 컨트롤러)
│   ├── Dao/
│   │   ├── MemberDao.java (회원 DAO)
│   │   └── BoardDao.java (게시판 DAO) ✓
│   ├── Dto/
│   │   ├── MemberDto.java
│   │   └── BoardDto.java ✓
│   └── service/
│       ├── MemberServiceImpl.java
│       ├── BoardService.java (인터페이스) ✓
│       └── BoardServiceImpl.java ✓
└── src/main/webapp/
    ├── main.jsp (메인 페이지)
    ├── member.jsp (회원 목록)
    ├── register.jsp (회원가입)
    ├── search.jsp (회원검색)
    ├── searchResult.jsp (검색 결과)
    ├── board.jsp (게시판) ✓
    └── writeForm.jsp (글쓰기)
```

## 3. 접속 URL

| 기능 | URL | 설명 |
|------|-----|------|
| 메인 페이지 | http://localhost:8080/p0205_06/main.do | 홈 |
| 회원 목록 | http://localhost:8080/p0205_06/member.do | 전체 회원 조회 |
| 회원 검색 | http://localhost:8080/p0205_06/search.do | 회원 검색 폼 |
| **게시판** | http://localhost:8080/p0205_06/login.do | 게시판 목록 ✓ |
| **게시판** | http://localhost:8080/p0205_06/board.do | 게시판 목록 ✓ |
| 글쓰기 | http://localhost:8080/p0205_06/writeForm.do | 게시글 작성 폼 |

## 4. 데이터베이스 컬럼 매핑

| 테이블 | 컬럼명 | 타입 | 설명 |
|--------|--------|------|------|
| board | no | NUMBER | 게시글 번호 (PK, 시퀀스) |
| board | title | VARCHAR2(100) | 게시글 제목 |
| board | writer | VARCHAR2(20) | 작성자 |
| board | writedate | DATE | 작성일 (기본값: SYSDATE) |
| board | views | NUMBER | 조회수 (기본값: 0) |
| board | content | CLOB | 게시글 내용 |
| board | pwd | VARCHAR2(20) | 비밀번호 |

## 5. 트러블슈팅

### 문제: HTTP 404 에러
**원인**: board 테이블이 없거나 board.jsp 파일이 없음
**해결**: 
1. board_table_init.sql 파일을 실행하여 테이블 생성
2. /webapp 폴더에 board.jsp 파일 확인

### 문제: "부적합한 열 이름" 에러
**원인**: 데이터베이스 컬럼명이 코드와 다름
**해결**: 위의 "데이터베이스 컬럼 매핑" 섹션 참고하여 테이블 생성

### 문제: "BoardServiceImpl - board list size: 0"
**원인**: 테이블은 있으나 데이터가 없음
**해결**: 샘플 데이터 삽입 SQL 실행

### 문제: DataSource 연결 실패
**원인**: context.xml에서 Oracle21 DataSource 정의 안됨
**해결**: Tomcat/conf/context.xml 파일 확인:
```xml
<Resource name="jdbc/Oracle21" 
          auth="Container"
          type="javax.sql.DataSource"
          driverClassName="oracle.jdbc.driver.OracleDriver"
          url="jdbc:oracle:thin:@localhost:1521:XE"
          username="scott"
          password="tiger"
          maxActive="20"
          maxIdle="10"
          maxWait="-1"/>
```

## 6. 테스트 순서

1. ✓ SQL 스크립트 실행 → board 테이블 생성 및 데이터 삽입
2. ✓ Tomcat 재시작
3. ✓ http://localhost:8080/p0205_06/main.do 접속
4. ✓ "게시판" 메뉴 클릭 → http://localhost:8080/p0205_06/login.do
5. ✓ 게시글 목록 표시 확인

## 7. 로그 확인

Tomcat 콘솔에서 다음 로그가 출력되는지 확인:

```
=== BoardDao Debug ===
Executing query: select no, title, writer, writedate, views, content, pwd from board order by no desc
Found Board: no=5, title=마지막 테스트 글
Found Board: no=4, title=데이터베이스 연동 성공
...
Total boards retrieved: 5

=== BoardServiceImpl Debug ===
BoardServiceImpl - board list size: 5
```

만약 에러 로그가 나타나면:
```
=== BoardDao selectAll Error ===
Error Message: [에러 메시지]
```
을 확인하고 해당 에러에 맞춰 조치하세요.
