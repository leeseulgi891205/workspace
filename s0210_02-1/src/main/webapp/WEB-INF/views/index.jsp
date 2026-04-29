<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>메인페이지</title>
	</head>
	<body>
		<h2>메인페이지</h2>
		<c:choose>
			<c:when test="${not empty member}">
				<p>환영합니다, ${member.id} 님</p>
			</c:when>
			<c:otherwise>
				<p>로그인되지 않았습니다.</p>
			</c:otherwise>
		</c:choose>
		<ul>
			<li><a href="/mupdate">회원정보수정</a></li>
			<li><a href="/boardView?bno=1">1번 게시글</a></li>
			<li><a href="/login">로그인</a></li>
			<li><a href="/join">회원가입</a></li>
			<li><a href="/board">게시판</a></li>
		</ul>
		
		<p>${nowFormatted}</p>
		<p><fmt:formatNumber value="3.141592" pattern="000.##"/></p>
		
	</body>
</html>