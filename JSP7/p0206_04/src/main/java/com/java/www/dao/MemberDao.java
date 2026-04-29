package com.java.www.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import com.java.www.dto.MemberDto;

public class MemberDao {
	//db연결정보선언
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	DataSource dataSource;
	String query;
	// dto에 맞는 변수
	String id,pw,name,phone,email,gender,hobby;
	List<MemberDto> list;
	MemberDto mdto;
	
	// 회원가입 저장 메소드
	public void memberInsert(String id, String pw, String name, 
			String phone,String email, String gender, String hobby) {
		conn = getConnection();
		query = "insert into member values ( ?,?,?,?,?,?,? )";
		try {
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, id);
			pstmt.setString(2, pw);
			pstmt.setString(3, name);
			pstmt.setString(4, phone);
			pstmt.setString(5, email);
			pstmt.setString(6, gender);
			pstmt.setString(7, hobby);
			int result = pstmt.executeUpdate();
			System.out.println("성공 : "+result);
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) {e2.printStackTrace();}
		}
	}//memberInsert
	
	
	//전체회원리스트 메소드
	public List<MemberDto> selectAll() {
		List<MemberDto> list = new ArrayList<MemberDto>();
		conn = getConnection();
		query = "select * from member order by id asc";
		try {
			pstmt = conn.prepareStatement(query);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				id = rs.getString("id");
				pw = rs.getString("pw");
				name = rs.getString("name");
				phone = rs.getString("phone");
				email = rs.getString("email");
				gender = rs.getString("gender");
				hobby = rs.getString("hobby");
				list.add(new MemberDto(id, pw, name, phone, email, gender, hobby));
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
	
	
	//로그인 메소드
	public MemberDto memberLogin(String id2, String pw2)  {
		try {
			conn = getConnection();
			query = "select * from member where id=? and pw=?";
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, id2);
			pstmt.setString(2, pw2);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				id = rs.getString("id");
				pw = rs.getString("pw");
				name = rs.getString("name");
				phone = rs.getString("phone");
				email = rs.getString("email");
				gender = rs.getString("gender");
				hobby = rs.getString("hobby");
				mdto = new MemberDto(id, pw, name, phone, email, gender, hobby);
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
		return mdto;
	}//
	
	
	
	
	
	//connection 연결메소드
	Connection getConnection() {
		Connection connection = null;
		try {
			Context context = new InitialContext();
			dataSource = (DataSource)context.lookup("java:comp/env/jdbc/Oracle21");
			connection = dataSource.getConnection();
		} catch (Exception e) {e.printStackTrace();}
		return connection; 
	}


	





	







	
	
	
	
	
	

}
