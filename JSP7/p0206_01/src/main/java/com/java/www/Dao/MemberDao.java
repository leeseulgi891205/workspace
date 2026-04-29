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
        // Context.xml 등에 설정된 이름과 일치해야 합니다. (예: jdbc/Oracle11g)
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
                String mhobby = rs.getString("hobby");

                memberDto = new MemberDto(mid, mpw, mname, mphone, memail, mgender, mhobby);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, rs);
        }
        
        return memberDto;
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