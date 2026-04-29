<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원정보</title>
<style>
h2{text-align:center;}
table, th, td{border:1px solid black; border-collapse:collapse;}
table{width:800px; margin:20px auto;}
th, td{height:40px; text-align:center;}
.nav{width:800px; margin:0 auto; text-align:center;}
.nav a{margin:0 10px;}
</style>
</head>
<body>

<h2>회원정보</h2>

<div class="nav">
    <a href="<c:url value='/main.do' />">메인페이지</a>
    <a href="<c:url value='/member.do' />">회원정보</a>
    <a href="<c:url value='/board.do' />">게시판</a>
</div>

<p style="text-align:center;">
    개수 : <c:out value="${memberList != null ? memberList.size() : 0}" />
</p>

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

    <c:choose>
        <c:when test="${empty memberList}">
            <tr>
                <td colspan="7">회원 데이터가 없습니다.</td>
            </tr>
        </c:when>
        <c:otherwise>
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
        </c:otherwise>
    </c:choose>
</table>

</body>
</html>
