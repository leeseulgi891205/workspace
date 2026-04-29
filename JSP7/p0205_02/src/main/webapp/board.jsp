<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>    
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>게시판</title>
		<style>
		  h2{text-align: center;}
		  table,th,td{border:1px solid black; border-collapse: collapse;}
		  table{width:900px; margin:20px auto;}
		  th,td{width:150px; height:40px; text-align: center;}
		</style>
	</head>
	<body>
	  <h2>게시판</h2>
	  <h3>게시글개수 : ${list.size() }</h3>
	  <table>
	     <tr>
	       <th>번호</th>
	       <th>제목</th>
	       <th>날짜</th>
	       <th>작성자</th>
	       <th>조회수</th>
	     </tr>
	     <!-- for문 -->
	     <c:forEach var="board" items="${list}">
	     <tr>
	       <td>${board.bno}</td>
	       <td>${board.btitle}</td>
	       <td>${board.bdate}</td>
	       <td>${board.id}</td>
	       <td>${board.bhit}</td>
	     </tr>
	     </c:forEach>
	     
	  </table>   
	
	</body>
</html>