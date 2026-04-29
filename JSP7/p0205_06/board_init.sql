-- 게시판 테이블 생성 (기존 테이블 삭제 후 재생성)
DROP TABLE board;
DROP SEQUENCE board_seq;

-- board 테이블 생성
CREATE TABLE board (
    no NUMBER PRIMARY KEY,
    title VARCHAR2(100) NOT NULL,
    writer VARCHAR2(20) NOT NULL,
    writedate DATE DEFAULT SYSDATE,
    view_cnt NUMBER DEFAULT 0,
    content CLOB NOT NULL,
    pwd VARCHAR2(20) NOT NULL
);

-- 시퀀스 생성
CREATE SEQUENCE board_seq
START WITH 1
INCREMENT BY 1;

-- 테스트 데이터 삽입
INSERT INTO board (no, title, writer, writedate, view_cnt, content, pwd) 
VALUES (board_seq.nextval, 'JSP 게시판 프로젝트', 'admin', SYSDATE, 5, 'JSP를 이용한 게시판 프로젝트입니다.', '1234');

INSERT INTO board (no, title, writer, writedate, view_cnt, content, pwd) 
VALUES (board_seq.nextval, '첫 번째 글입니다', 'user01', SYSDATE, 3, '안녕하세요. 이것은 첫 번째 게시글입니다.', '5678');

INSERT INTO board (no, title, writer, writedate, view_cnt, content, pwd) 
VALUES (board_seq.nextval, '게시판 테스트', 'user02', SYSDATE, 2, '게시판이 정상적으로 작동하는지 테스트합니다.', '9876');

INSERT INTO board (no, title, writer, writedate, view_cnt, content, pwd) 
VALUES (board_seq.nextval, '데이터베이스 연동 성공', 'user03', SYSDATE, 1, 'JSP에서 데이터베이스 연동이 성공적으로 이루어졌습니다.', '5432');

INSERT INTO board (no, title, writer, writedate, view_cnt, content, pwd) 
VALUES (board_seq.nextval, '마지막 테스트 글', 'user04', SYSDATE, 0, '이것이 마지막 테스트 글입니다.', '1111');

COMMIT;

-- 데이터 확인
SELECT * FROM board ORDER BY no DESC;
