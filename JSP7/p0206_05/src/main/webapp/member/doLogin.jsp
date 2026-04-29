<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>로그인 처리</title>
	</head>
	<body>
	<script>
		<c:if test="${login == 1}">
			alert("로그인 성공했습니다.");
			location.href="index.do";
		</c:if>
		<c:if test="${login == 0}">
			alert("아이디 또는 비밀번호가 잘못되었습니다.");
			location.href="login.do";
		</c:if>
	</script>
	</body>
</html>
