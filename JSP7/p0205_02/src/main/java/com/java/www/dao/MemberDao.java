package com.java.www.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

import com.java.www.dto.MemberDto;

public class MemberDao {
	
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	DataSource dataSource;
	String query;
	String id,pw,name,phone,email,gender,hobby;
	
	//생성자
	public MemberDao() {
		try {
			Context context = new InitialContext();
			dataSource = (DataSource)context.lookup("java:comp/env/jdbc/Oracle21");
		} catch (NamingException e) {e.printStackTrace();}
	}
	
	//회원전체리스트 메소드선언
	public List<MemberDto> memberList(){
		List<MemberDto> list = new ArrayList<MemberDto>();
		try {
			conn = dataSource.getConnection();
			query = "select * from member";
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
				list.add(new MemberDto(id,pw,name,phone,email,gender,hobby));
			}
		} catch (Exception e) {e.printStackTrace();}
		finally {
			try {
				if(rs!=null) rs.close();
				if(pstmt!=null) pstmt.close();
				if(conn!=null) conn.close();
			} catch (Exception e2) { e2.printStackTrace();	}
		}
		return list;
	}//memberList
	
	
	

}
