package com.java.www.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import com.java.www.dto.BoardDto;

public class BoardDao {

	//db연결정보선언
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	DataSource dataSource;
	String query;
	// dto에 맞는 변수
	int bno,bgroup,bstep,bindent,bhit;
	String btitle,bcontent,id,bfile;
	Timestamp bdate;
	List<BoardDto> list;
	BoardDto bdto;
	
	// 게시글1개 메소드
	public BoardDto selectOne(int bno) {
		bdto = null;
		conn = getConnection();
		String query = "select * from board where bno=?";
		
		try {
			pstmt = conn.prepareStatement(query);
			pstmt.setInt(1, bno);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				btitle = rs.getString("btitle");
				bcontent = rs.getString("bcontent");
				id = rs.getString("id");
				bgroup = rs.getInt("bgroup");
				bstep = rs.getInt("bstep");
				bindent = rs.getInt("bindent");
				bhit = rs.getInt("bhit");
				bfile = rs.getString("bfile");
				bdate = rs.getTimestamp("bdate");
				bdto = new BoardDto(bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile, bdate);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
		
		return bdto;
	}

	
	
	// 전체게시글리스트 메소드
	public List<BoardDto> selectAll() {
		List<BoardDto> list = new ArrayList<BoardDto>();
		conn = getConnection();
		query = "select * from board order by bgroup desc,bstep asc";
		try {
			pstmt = conn.prepareStatement(query);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				bno = rs.getInt("bno");
				btitle = rs.getString("btitle");
				bcontent = rs.getString("bcontent");
				id = rs.getString("id");
				bgroup = rs.getInt("bgroup");
				bstep = rs.getInt("bstep");
				bindent = rs.getInt("bindent");
				bhit = rs.getInt("bhit");
				bfile = rs.getString("bfile");
				bdate = rs.getTimestamp("bdate");
				list.add(new BoardDto(bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile, bdate));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
		

		
		return list;
	}//selectAll
	
	
	// 게시글 저장 메소드
	public void boardInsert(String btitle, String bcontent, String id, String bfile) {
		conn = getConnection();
		query = "insert into board(bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile, bdate) " +
				"values(board_seq.nextval, ?, ?, ?, board_seq.currval, 0, 0, 0, ?, sysdate)";
		try {
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, btitle);
			pstmt.setString(2, bcontent);
			pstmt.setString(3, id);
			pstmt.setString(4, bfile);
			pstmt.executeUpdate();
			System.out.println("[DEBUG] Board insert successful");
		} catch (SQLException e) {
			System.err.println("[ERROR] Board insert failed:");
			e.printStackTrace();
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
	}//boardInsert
	
	// 게시글 수정 메소드
	public void boardUpdate(int bno, String btitle, String bcontent, String bfile) {
		conn = getConnection();
		query = "update board set btitle=?, bcontent=?, bfile=? where bno=?";
		try {
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, btitle);
			pstmt.setString(2, bcontent);
			pstmt.setString(3, bfile);
			pstmt.setInt(4, bno);
			pstmt.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
	}
	
	// 게시글 삭제 메소드
	public void boardDelete(int bno) {
		conn = getConnection();
		query = "delete from board where bno=?";
		try {
			pstmt = conn.prepareStatement(query);
			pstmt.setInt(1, bno);
			pstmt.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
	}
	
	//connection 연결메소드
	Connection getConnection() {
		Connection connection = null;
		try {
			System.out.println("[DEBUG] Starting DB Connection...");
			Context context = new InitialContext();
			System.out.println("[DEBUG] InitialContext created successfully");
			
			dataSource = (DataSource)context.lookup("java:comp/env/jdbc/Oracle21");
			System.out.println("[DEBUG] DataSource lookup successful: " + dataSource);
			
			connection = dataSource.getConnection();
			System.out.println("[DEBUG] Connection obtained: " + connection);
		} catch (Exception e) {
			System.err.println("[ERROR] Failed to get DB connection:");
			e.printStackTrace();
			
			// Fallback: 직접 연결 시도
			try {
				System.out.println("[DEBUG] Attempting direct JDBC connection...");
				Class.forName("oracle.jdbc.OracleDriver");
				connection = java.sql.DriverManager.getConnection(
					"jdbc:oracle:thin:@localhost:1521:xe", 
					"ora_user", 
					"1111"
				);
				System.out.println("[DEBUG] Direct connection successful: " + connection);
			} catch (Exception e2) {
				System.err.println("[ERROR] Direct connection also failed:");
				e2.printStackTrace();
			}
		}
		return connection; 
	}

}//class