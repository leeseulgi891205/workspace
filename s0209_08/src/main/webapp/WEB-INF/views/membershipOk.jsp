<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>회원가입 확인</title>
	</head>
	<body>
		<h2>회원가입 확인 - 넘어온 데이터</h2>
		<h2>아이디 확인 : ${id }</h2>
		<h3>비밀번호 확인 : ${pw}</h3>
        <h3>이름 : ${name}</h3>
        <h3>전화번호 : ${phone}</h3>
        <h3>이메일 확인 : ${email}</h3>
        <h3>성별 : ${gender}</h3>
        <h3>관심사 : ${hobby}</h3>
        <a href="/">홈으로</a>
	</body>
</html>