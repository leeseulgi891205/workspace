
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ page import="java.sql.Connection, java.sql.PreparedStatement, java.sql.ResultSet" %>
<%@ page import="javax.naming.Context, javax.naming.InitialContext" %>
<%@ page import="javax.sql.DataSource" %>




<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>메인페이지</title>
</head>
<body>
    <h2>메인페이지</h2>

    <%-- jsp 5가지 태그 --%>
    <%--
        1. 스크립틀릿 태그 - <%  %>
        2. 표현식 태그 - <%=  %>
        3. 선언 태그 - <%!  %>
        4. 지시자 태그 - <%@  %>
        5. 주석 태그 - <%-- --%>
    

    <%
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        String id = "", pw="", name="", phone="", email="", gender="" , hobby="";

        try {
            Context init = new InitialContext();
            DataSource ds = (DataSource)init.lookup("java:comp/env/jdbc/Oracle21");
            //db연결
            conn = ds.getConnection();
            String query = "SELECT * FROM member";
            //sql구문 실행
            pstmt = conn.prepareStatement(query);
            //결과값 리턴
            rs = pstmt.executeQuery();
            while (rs.next()) {
            	
            	
            	// 실수 : bno = rs.getDouble("bdouble");
            	// 정수 : bdouble = rs.getInt("bdouble");
            	// 날짜 : bdate = rs.getDate("bdate");
            	
            	
                id = rs.getString("id");
                pw = rs.getString("pw");
                name = rs.getString("name");
                phone = rs.getString("phone");
                email = rs.getString("email");
                gender = rs.getString("gender");
                hobby = rs.getString("hobby");
                out.println("ID: " + id + ", PW: " + pw + ", Name: " + name + ", Phone: "
                			+ phone + ", Email: " + gender + ", Hobby: " + hobby + "<br>");
            }

        } catch (Exception e) {
            e.printStackTrace(); 
        } finally {
            try { if (rs != null) rs.close(); } catch (Exception e) {}
            try { if (pstmt != null) pstmt.close(); } catch (Exception e) {}
            try { if (conn != null) conn.close(); } catch (Exception e) {
                e.printStackTrace(); 
            }
        }

        for (int i = 1; i <= 10; i++) {
            out.println(i + "<br>");
        }
    %>

</body>
</html>
