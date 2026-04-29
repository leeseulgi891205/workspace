-- Member 테이블 생성
CREATE TABLE member (
    id VARCHAR2(20) PRIMARY KEY,
    pw VARCHAR2(20) NOT NULL,
    name VARCHAR2(50),
    phone VARCHAR2(20),
    email VARCHAR2(100),
    gender VARCHAR2(1),
    hobby VARCHAR2(200),
    reg_date DATE DEFAULT SYSDATE
);

-- 테스트 데이터 삽입
INSERT INTO member (id, pw, name, phone, email, gender, hobby) 
VALUES ('aaa', '1111', '홍길동', '010-1111-1111', 'hong@email.com', 'M', '게임,골프');

INSERT INTO member (id, pw, name, phone, email, gender, hobby) 
VALUES ('bbb', '2222', '이순신', '010-2222-2222', 'lee@email.com', 'M', '독서,운동');

INSERT INTO member (id, pw, name, phone, email, gender, hobby) 
VALUES ('ccc', '3333', '강감찬', '010-3333-3333', 'kang@email.com', 'M', '수영,드라이브');

COMMIT;

-- 테이블 조회
SELECT * FROM member;
