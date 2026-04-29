<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>게시글 보기</title>
</head>
<body>
    <h2>게시글 상세</h2>
    <c:choose>
        <c:when test="${not empty board}">
            <h3>글번호: ${board.bno}</h3>
            <h3>제목: ${board.btitle}</h3>
            <h3>내용: ${board.bcontent}</h3>
            <h3>작성자: ${board.id}</h3>
        </c:when>
        <c:otherwise>
            <p>표시할 게시글이 없습니다. 목록에서 게시글을 선택하세요.</p>
        </c:otherwise>
    </c:choose>
    <ul>
        <li><a href="/">홈으로</a></li>
        <li><a href="/board">게시글 작성</a></li>
    </ul>
</body>
</html>
