package com.java.www.Dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import com.java.www.Dto.BoardDto;

public class BoardDao {
	
	// db정보선언
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	DataSource dataSource;
	String query;
	
	public BoardDao() {
		try {
			Context context = new InitialContext();
			dataSource = (DataSource) context.lookup("java:comp/env/jdbc/Oracle21");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	// 게시글 전체 리스트 가져오기
	public List<BoardDto> selectAll() {
		List<BoardDto> list = new ArrayList<BoardDto>();
		try {
			conn = dataSource.getConnection();
			// 게시판 전체 리스트 (최신순으로 정렬)
			// 모든 컬럼을 조회하되, 컬럼명을 명시적으로 지정
			query = "select no, title, writer, writedate, views, content, pwd from board order by no desc";
			System.out.println("=== BoardDao Debug ===");
			System.out.println("Executing query: " + query);
			pstmt = conn.prepareStatement(query);
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				int no = rs.getInt("no");
				String title = rs.getString("title");
				String writer = rs.getString("writer");
				String writedate = rs.getString("writedate");
				int views = rs.getInt("views");
				
				System.out.println("Found Board: no=" + no + ", title=" + title);
				list.add(new BoardDto(no, title, writer, writedate, views));
			}
			System.out.println("Total boards retrieved: " + list.size());
		
		} catch (Exception e) {
			System.out.println("=== BoardDao selectAll Error ===");
			System.out.println("Error Message: " + e.getMessage());
			System.out.println("가능한 해결책:");
			System.out.println("1. 데이터베이스 테이블의 컬럼명 확인");
			System.out.println("2. board 테이블이 존재하는지 확인");
			System.out.println("3. 아래 SQL을 실행하여 테이블 생성:");
			System.out.println("   CREATE TABLE board (");
			System.out.println("       no NUMBER PRIMARY KEY,");
			System.out.println("       title VARCHAR2(100) NOT NULL,");
			System.out.println("       writer VARCHAR2(20) NOT NULL,");
			System.out.println("       writedate DATE DEFAULT SYSDATE,");
			System.out.println("       views NUMBER DEFAULT 0,");
			System.out.println("       content CLOB NOT NULL,");
			System.out.println("       pwd VARCHAR2(20) NOT NULL");
			System.out.println("   );");
			e.printStackTrace();
		} finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return list;
	}
	
	// 게시글 목록 - selectAll의 별칭
	public List<BoardDto> boardList() {
		return selectAll();
	}
	
	// 게시글 상세 조회
	public BoardDto selectOne(int no) {
		BoardDto board = null;
		try {
			conn = dataSource.getConnection();
			query = "select no, title, writer, writedate, views, content, pwd from board where no = ?";
			pstmt = conn.prepareStatement(query);
			pstmt.setInt(1, no);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				int boardNo = rs.getInt("no");
				String title = rs.getString("title");
				String writer = rs.getString("writer");
				String writedate = rs.getString("writedate");
				int views = rs.getInt("views");
				String content = rs.getString("content");
				String pwd = rs.getString("pwd");
				
				board = new BoardDto(boardNo, title, writer, writedate, views, content, pwd);
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return board;
	}
	
	// 게시글 등록
	public int insert(BoardDto board) {
		int result = 0;
		try {
			conn = dataSource.getConnection();
			query = "insert into board(no, title, writer, writedate, views, content, pwd) "
					+ "values(board_seq.nextval, ?, ?, sysdate, 0, ?, ?)";
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, board.getTitle());
			pstmt.setString(2, board.getWriter());
			pstmt.setString(3, board.getContent());
			pstmt.setString(4, board.getPwd());
			
			result = pstmt.executeUpdate();
			
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		return result;
	}
}
