<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ page import="java.sql.Connection, java.sql.PreparedStatement, java.sql.ResultSet, java.sql.Timestamp" %>
<%@ page import="javax.naming.Context, javax.naming.InitialContext" %>
<%@ page import="javax.sql.DataSource" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>메인페이지</title>
</head>
<body>
    <h2>MEMBER 출력</h2>

<%
    Connection conn = null;
    PreparedStatement pstmt = null;
    ResultSet rs = null;

    try {
        Context init = new InitialContext();
        DataSource ds = (DataSource)init.lookup("java:comp/env/jdbc/Oracle21");

        conn = ds.getConnection();

        
        String query = "SELECT id, pw, name, phone, email, gender, hobby, regdate FROM member";

        pstmt = conn.prepareStatement(query);
        //insert,update,delete -> executeUpdate();
        rs = pstmt.executeQuery();

        while (rs.next()) {
            String id = rs.getString("id");
            String pw = rs.getString("pw");
            String name = rs.getString("name");
            String phone = rs.getString("phone");
            String email = rs.getString("email");
            String gender = rs.getString("gender");
            String hobby = rs.getString("hobby");
            Timestamp regdate = rs.getTimestamp("regdate");

            out.println(
                "ID: " + id +
                ", PW: " + pw +
                ", Name: " + name +
                ", Phone: " + phone +
                ", Email: " + email +
                ", Gender: " + gender +
                ", Hobby: " + hobby +
                ", RegDate: " + regdate +
                "<br>"
            );
        }

    } catch (Exception e) {
        e.printStackTrace();
        out.println("<p>에러: " + e.getMessage() + "</p>");
    } finally {
        try { if (rs != null) rs.close(); } catch (Exception e) {}
        try { if (pstmt != null) pstmt.close(); } catch (Exception e) {}
        try { if (conn != null) conn.close(); } catch (Exception e) {}
    }
%>

</body>
</html>
