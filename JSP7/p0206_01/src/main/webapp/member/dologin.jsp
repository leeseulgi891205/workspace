<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>로그인 처리</title>
</head>
<body>
    <script>
        if (${empty mdto}) {
            alert("아이디 또는 비밀번호가 일치하지 않습니다.");
            location.href = "login.do";
        } else {
            alert("로그인이 되었습니다.");
            location.href = "main.do"; 
        }
    </script>
</body>
</html>