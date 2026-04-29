<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>    
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
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
	  <!-- list : request -->
	  <h3>리스트개수 : ${list.size() }</h3>
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
	     <c:forEach var="member" items="${list}">
	     <tr>
	       <td>${member.id}</td>
	       <td>${member.pw}</td>
	       <td>${member.name}</td>
	       <td>${member.phone}</td>
	       <td>${member.email}</td>
	       <td>${member.gender}</td>
	       <td>${member.hobby}</td>
	     </tr>
	     </c:forEach>
	     
	  </table>   
	
	</body>
</html>