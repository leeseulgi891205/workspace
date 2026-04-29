package com.java.www.Dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.sql.DataSource;
import javax.naming.Context;
import javax.naming.InitialContext;
import com.java.www.Dto.MemberDto;

public class MemberDao {
    
    private Connection conn;
    private PreparedStatement pstmt;
    private ResultSet rs;
    private String query;

    public MemberDao() {}

    private Connection getConnection() throws Exception {
        Context context = new InitialContext();
        DataSource ds = (DataSource) context.lookup("java:comp/env/jdbc/Oracle11g");
        return ds.getConnection();
    }

    public MemberDto memberLogin(String id, String pw) {
        MemberDto memberDto = null;
        
        try {
            conn = getConnection();
            query = "SELECT * FROM member WHERE id=? AND pw=?";
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, id);
            pstmt.setString(2, pw);
            rs = pstmt.executeQuery();
            
            if (rs.next()) {
                String mid = rs.getString("id");
                String mpw = rs.getString("pw");
                String mname = rs.getString("name");
                String mphone = rs.getString("phone");
                String memail = rs.getString("email");
                String mgender = rs.getString("gender");

                memberDto = new MemberDto(mid, mpw, mname, mphone, memail, mgender);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, rs);
        }
        
        return memberDto;
    }
    
    public boolean memberInsert(String id, String pw, String name, String phone, String email, String gender, String hobby) {
        boolean result = false;
        
        try {
            conn = getConnection();
            query = "INSERT INTO member (id, pw, name, phone, email, gender, hobby) VALUES (?, ?, ?, ?, ?, ?, ?)";
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, id);
            pstmt.setString(2, pw);
            pstmt.setString(3, name);
            pstmt.setString(4, phone);
            pstmt.setString(5, email);
            pstmt.setString(6, gender);
            pstmt.setString(7, hobby);
            
            int count = pstmt.executeUpdate();
            
            if (count > 0) {
                result = true;
                System.out.println("[회원가입 성공] ID: " + id + ", Name: " + name);
            }
        } catch (Exception e) {
            System.out.println("[회원가입 실패] " + e.getMessage());
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, null);
        }
        
        return result;
    }

    private void closeResources(Connection conn, PreparedStatement pstmt, ResultSet rs) {
        try {
            if (rs != null) rs.close();
            if (pstmt != null) pstmt.close();
            if (conn != null) conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}


