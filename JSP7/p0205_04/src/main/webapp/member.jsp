<%@page import="com.java.www.dto.MemberDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>회원정보</title>
	<style>
		  h2{text-align: center;}
		  table,th,td{border:1px solid black; border-collapse: collapse;}
		  table{width:900px; margin:20px auto;}
		  th,td{width:150px; height:40px; text-align: center;}
	</style>
</head>
<body>

	<h2>회원정보</h2>
		<p><a href="main.do">메인페이지</a></p>
		<p><a href="member.do">회원정보</a></p>
		<p><a href="board.do">게시판</a></p>
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
	     <!-- for문 -->
	     <c:forEach var="mem" items="${list}">
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
	

</body>
</html>