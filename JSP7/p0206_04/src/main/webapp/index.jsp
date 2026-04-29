<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>    
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>메인페이지</title>
	</head>
	<body>
	  <h2>메인페이지</h2>
	  <ul>
	    <!-- 로그인전 -->
	    <c:if test="${session_id == null }">
	    <li><a href="./login.do">로그인</a></li>
	    <li><a href="./membership.do">회원가입</a></li>
	    </c:if>
	    
	    <c:if test="${session_id != null }">
	    <!-- 로그인후 -->
	    <li><a href="./logout.do">로그아웃</a></li>
	    <li><a href="./member.do">회원전체정보</a></li>
	    <li><a href="./board.do">게시판정보</a></li>
	    </c:if>
	  </ul>
	
	</body>
</html>