-- ============================================
-- 게시판(board) 테이블 초기화 스크립트
-- ============================================

-- 기존 테이블 및 시퀀스 삭제 (존재하면)
DROP TABLE board CASCADE CONSTRAINTS;
DROP SEQUENCE board_seq;

-- board 테이블 생성
CREATE TABLE board (
    no          NUMBER          PRIMARY KEY,
    title       VARCHAR2(100)   NOT NULL,
    writer      VARCHAR2(20)    NOT NULL,
    writedate   DATE            DEFAULT SYSDATE,
    views       NUMBER          DEFAULT 0,
    content     CLOB            NOT NULL,
    pwd         VARCHAR2(20)    NOT NULL
);

-- 시퀀스 생성 (board_seq: board 테이블의 no 컬럼 자동증가)
CREATE SEQUENCE board_seq
    START WITH 1
    INCREMENT BY 1
    NOCACHE;

-- ============================================
-- 테스트용 샘플 데이터 삽입
-- ============================================

INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, 'JSP 게시판 프로젝트', 'admin', SYSDATE, 5, 
'JSP와 Oracle을 이용한 게시판 프로젝트입니다. 이 프로젝트는 MVC 패턴을 따르고 있습니다.', '1234');

INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, '첫 번째 글입니다', 'user01', SYSDATE-1, 3, 
'안녕하세요. 이것은 첫 번째 게시글입니다. 게시판이 정상적으로 작동하고 있습니다.', '5678');

INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, '게시판 테스트', 'user02', SYSDATE-2, 2, 
'게시판이 정상적으로 작동하는지 테스트합니다. 데이터베이스 연동이 완료되었습니다.', '9876');

INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, '데이터베이스 연동 성공', 'user03', SYSDATE-3, 1, 
'JSP에서 데이터베이스 연동이 성공적으로 이루어졌습니다. board 테이블이 정상입니다.', '5432');

INSERT INTO board (no, title, writer, writedate, views, content, pwd) 
VALUES (board_seq.nextval, '마지막 테스트 글', 'user04', SYSDATE-4, 0, 
'이것이 마지막 테스트 글입니다. 모든 기능이 정상적으로 작동합니다.', '1111');

-- 데이터 커밋
COMMIT;

-- ============================================
-- 확인 쿼리 (실행 후 데이터 확인)
-- ============================================
SELECT COUNT(*) as 전체글개수 FROM board;
SELECT no, title, writer, writedate, views FROM board ORDER BY no DESC;
