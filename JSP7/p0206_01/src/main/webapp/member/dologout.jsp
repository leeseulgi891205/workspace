<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    if (session != null) {
        session.invalidate();
    }
%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>로그아웃 처리</title>
</head>
<body>
    <script>
        alert("로그아웃 되었습니다.");
        location.href = "main.do";
    </script>
</body>
</html>