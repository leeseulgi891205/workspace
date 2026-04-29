package com.java.www.Dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import com.java.www.Dto.MemberDto;

public class MemberDao {
	
	//db정보선언
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	DataSource dataSource;
	String id, pw, name, phone, email, gender, hobby;
	String query;
	
	public MemberDao() {
		try {
			Context context = new InitialContext();
			dataSource = (DataSource) context.lookup("java:comp/env/jdbc/Oracle21");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	//회원 전체리스트 가져오기
	public List<MemberDto> selectAll() {
		List<MemberDto> list = new ArrayList<MemberDto>();
		// db연결 검색
		try {
			conn = dataSource.getConnection();
			// 회원 전체 리스트
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
				list.add(new MemberDto(id, pw, name,phone, email, gender, hobby));
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
		return list;
	}
	
	public List<MemberDto> memberList() {
		return selectAll();
	}
}
