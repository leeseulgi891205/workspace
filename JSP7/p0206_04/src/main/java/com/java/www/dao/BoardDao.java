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




	
	
	
}//class
