<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Insert title here</title>
	</head>
	<body>
	<script>
		if(${mdto == null}){
			alert("아이디 또는 패스워드가 일치하지 않습니다.");
			location.href="login.do";
		}else{
			alert("로그인이 되었습니다.");
			location.href="index.do";
		}		
	</script>
	
	</body>
</html>