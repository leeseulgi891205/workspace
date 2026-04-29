package com.java.www.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import com.java.www.dto.MemberDto;

public class MemberDao {
	
	Connection conn;	// DB 연결 객체
	PreparedStatement pstmt;	// SQL 실행 객체
	ResultSet rs;	// SQL 결과 객체
	DataSource dataSource;	// SQL 쿼리 문자열
	String query;	// SQL 쿼리 문자열
	
	// 로그인 - 회원 정보 조회
	public MemberDto selectOne(String id, String pw) {
		MemberDto mdto = null;	// 회원 정보 DTO 객체 초기화
		conn = getConnection();	// DB 연결 메서드 호출
		query = "select * from member where id=? and pw=?";	// SQL 쿼리 문자열
		
		try {
			pstmt = conn.prepareStatement(query);	// SQL 실행 객체 생성
			pstmt.setString(1, id);	// 첫 번째 물음표에 id 설정
			pstmt.setString(2, pw);	// 두 번째 물음표에 pw 설정
			rs = pstmt.executeQuery();	// SQL 쿼리 실행 및 결과 저장
			
			if(rs.next()) {
				String name = rs.getString("name");	// 회원 이름 조회
				String phone = rs.getString("phone");	// 회원 전화번호 조회
				String email = rs.getString("email");	// 회원 이메일 조회
				String gender = rs.getString("gender");	// 회원 성별 조회
				String hobby = rs.getString("hobby");	// 회원 취미 조회
				mdto = new MemberDto(id, pw, name, phone, email, gender, hobby);	// 회원 정보 DTO 객체 생성
				System.out.println("[DEBUG] Login successful for id: " + id);	// 디버그 메시지 출력
			} else {
				System.out.println("[DEBUG] Login failed - invalid id or password");	// 디버그 메시지 출력
			}
		} catch (Exception e) {
			System.err.println("[ERROR] Login query failed:");	// 에러 메시지 출력
			e.printStackTrace();	// 예외 발생 시 스택 트레이스 출력
		} finally {	// 자원 해제
			try {	// 자원 해제
				if(rs!=null) rs.close();	// 결과 객체 닫기
				if(pstmt!=null) pstmt.close();	// SQL 실행 객체 닫기
				if(conn!=null) conn.close();	// DB 연결 객체 닫기
			} catch (Exception e2) {e2.printStackTrace();}	// 예외 발생 시 스택 트레이스 출력
		}
		
		return mdto;
	}
	
	// 회원가입 - 회원 정보 저장
	public void memberInsert(String id, String pw, String name, String phone, String email, String gender, String hobby) {
		conn = getConnection();
		query = "insert into member(id, pw, name, phone, email, gender, hobby) values(?, ?, ?, ?, ?, ?, ?)";
		
		try {
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, id);
			pstmt.setString(2, pw);
			pstmt.setString(3, name);
			pstmt.setString(4, phone);
			pstmt.setString(5, email);
			pstmt.setString(6, gender);
			pstmt.setString(7, hobby);
			pstmt.executeUpdate();
			System.out.println("[DEBUG] Member insert successful for id: " + id);
		} catch (SQLException e) {
			System.err.println("[ERROR] Member insert failed:");
			e.printStackTrace();
		} finally {
			try {
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
	}
	
	// Connection 연결 메서드
	Connection getConnection() {
		Connection connection = null;	// DB 연결 객체 초기화
		try {
			System.out.println("[DEBUG] Starting DB Connection...");	// 디버그 메시지 출력
			Context context = new InitialContext(); // 초기 컨텍스트 생성
			System.out.println("[DEBUG] InitialContext created successfully");	// 디버그 메시지 출력
			
			dataSource = (DataSource)context.lookup("java:comp/env/jdbc/Oracle21");	// DataSource 조회
			System.out.println("[DEBUG] DataSource lookup successful: " + dataSource);	// 디버그 메시지 출력
			
			connection = dataSource.getConnection();	// DB 연결 객체 얻기
			System.out.println("[DEBUG] Connection obtained: " + connection);	// 디버그 메시지 출력
		} catch (Exception e) {
			System.err.println("[ERROR] Failed to get DB connection:");	// 에러 메시지 출력
			e.printStackTrace();	// 예외 발생 시 스택 트레이스 출력
			
			// Fallback: 직접 연결 시도
			try {
				System.out.println("[DEBUG] Attempting direct JDBC connection...");	// 디버그 메시지 출력
				Class.forName("oracle.jdbc.OracleDriver");	// Oracle JDBC 드라이버 로드
				connection = java.sql.DriverManager.getConnection(	// 직접 연결 시도
					"jdbc:oracle:thin:@localhost:1521:xe", // JDBC URL
					"ora_user", 	// DB 사용자 이름
					"1111"	// DB 비밀번호
				);
				System.out.println("[DEBUG] Direct connection successful: " + connection);	// 디버그 메시지 출력
			} catch (Exception e2) {	// 직접 연결 실패 시 예외 처리
				System.err.println("[ERROR] Direct connection also failed:");	// 에러 메시지 출력
				e2.printStackTrace();	// 예외 발생 시 스택 트레이스 출력
			}
		}
		return connection;
	}

}