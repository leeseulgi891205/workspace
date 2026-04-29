<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%@ page import="javax.sql.*" %>
<%@ page import="javax.naming.*" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>DB Connection Test</title>
</head>
<body>
    <h2>데이터베이스 연결 테스트</h2>
    
    <h3>1. JNDI DataSource 테스트</h3>
    <%
    Connection conn = null;
    try {
        out.println("<p>InitialContext 생성 시도...</p>");
        Context context = new InitialContext();
        out.println("<p style='color:green;'>✓ InitialContext 생성 성공</p>");
        
        out.println("<p>DataSource lookup 시도 (java:comp/env/jdbc/Oracle21)...</p>");
        DataSource ds = (DataSource)context.lookup("java:comp/env/jdbc/Oracle21");
        out.println("<p style='color:green;'>✓ DataSource lookup 성공: " + ds + "</p>");
        
        out.println("<p>Connection 획득 시도...</p>");
        conn = ds.getConnection();
        out.println("<p style='color:green;'>✓ Connection 획득 성공!</p>");
        out.println("<p style='color:blue;'>Connection 정보: " + conn + "</p>");
        
        // 간단한 쿼리 테스트
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT 'DB 연결 완료!' as msg FROM dual");
        if(rs.next()) {
            out.println("<p style='color:green;font-weight:bold;'>✓ " + rs.getString("msg") + "</p>");
        }
        rs.close();
        stmt.close();
        
    } catch(Exception e) {
        out.println("<p style='color:red;'>✗ JNDI 연결 실패:</p>");
        out.println("<pre style='color:red;'>");
        e.printStackTrace(new java.io.PrintWriter(out));
        out.println("</pre>");
    } finally {
        if(conn != null) try { conn.close(); } catch(Exception e) {}
    }
    %>
    
    <hr>
    
    <h3>2. 직접 JDBC 연결 테스트</h3>
    <%
    conn = null;
    try {
        out.println("<p>Oracle JDBC Driver 로딩 시도...</p>");
        Class.forName("oracle.jdbc.OracleDriver");
        out.println("<p style='color:green;'>✓ Driver 로딩 성공</p>");
        
        out.println("<p>Connection 획득 시도...</p>");
        conn = DriverManager.getConnection(
            "jdbc:oracle:thin:@localhost:1521:xe", 
            "ora_user", 
            "1111"
        );
        out.println("<p style='color:green;'>✓ 직접 Connection 획득 성공!</p>");
        out.println("<p style='color:blue;'>Connection 정보: " + conn + "</p>");
        
        // 간단한 쿼리 테스트
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT 'DB 연결 완료!' as msg FROM dual");
        if(rs.next()) {
            out.println("<p style='color:green;font-weight:bold;'>✓ " + rs.getString("msg") + "</p>");
        }
        rs.close();
        stmt.close();
        
    } catch(Exception e) {
        out.println("<p style='color:red;'>✗ 직접 연결 실패:</p>");
        out.println("<pre style='color:red;'>");
        e.printStackTrace(new java.io.PrintWriter(out));
        out.println("</pre>");
    } finally {
        if(conn != null) try { conn.close(); } catch(Exception e) {}
    }
    %>
    
    <hr>
    <p><a href="index.jsp">메인으로 돌아가기</a></p>
</body>
</html>
