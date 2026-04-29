<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>검색 결과</title>
	<style>
		body { font-family: Arial, sans-serif; padding: 20px; }
		h2 { text-align: center; color: #333; }
		.container { max-width: 900px; margin: 30px auto; }
		table, th, td { border: 1px solid black; border-collapse: collapse; }
		table { width: 100%; }
		th, td { padding: 12px; text-align: center; }
		th { background-color: rgb(0, 0, 0); color: white; }
		tr:nth-child(even) { background-color: #f2f2f2; }
		.no-result { text-align: center; padding: 30px; font-size: 16px; color: #666; }
		.btn-group { text-align: center; margin-top: 20px; }
		a, button { 
			display: inline-block;
			padding: 10px 20px;
			margin: 5px;
			background-color: rgb(0, 0, 0); 
			color: white; 
			text-decoration: none;
			border: none;
			border-radius: 3px;
			cursor: pointer;
			font-size: 14px;
		}
		a:hover, button:hover { background-color: rgb(0, 0, 0); }
		.search-info {
			background-color: #f9f9f9;
			padding: 15px;
			border-radius: 3px;
			margin-bottom: 20px;
			text-align: center;
		}
	</style>
</head>
<body>
	<h2>검색 결과</h2>
	<div class="container">
		<div class="search-info">
			<p>검색 아이디: <strong>${searchId}</strong></p>
		</div>
		
		<c:if test="${not empty memberList}">
			<table>
				<tr>
					<th>아이디</th>
					<th>패스워드</th>
					<th>이름</th>
					<th>전화번호</th>
					<th>이메일</th>
					<th>성별</th>
					<th>취미</th>
				</tr>
				<c:forEach var="mem" items="${memberList}">
					<tr>
						<td>${mem.id}</td>
						<td>${mem.pw}</td>
						<td>${mem.name}</td>
						<td>${mem.phone}</td>
						<td>${mem.email}</td>
						<td>${mem.gender}</td>
						<td>${mem.hobby}</td>
					</tr>
				</c:forEach>
			</table>
		</c:if>
		
		<c:if test="${empty memberList}">
			<div class="no-result">
				<p>검색 결과가 없습니다.</p>
				<p>"${searchId}"에 해당하는 회원이 없습니다.</p>
			</div>
		</c:if>
		
		<div class="btn-group">
			<a href="search.do">다시 검색</a>
			<a href="member.do">전체 회원 조회</a>
			<a href="main.do">메인 페이지</a>
		</div>
	</div>
</body>
</html>
