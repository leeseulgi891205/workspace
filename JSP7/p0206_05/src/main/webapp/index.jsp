<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메인페이지</title>
<style>
    body {margin: 0;
        font-family: Arial, sans-serif;
        }
        
    .header {background: #222; color: #fff;
        padding: 15px 30px; display: flex;
        justify-content: space-between; 
        align-items: center;
        }
        
    .logo {font-size: 20px;
        font-weight: bold;}
    .nav a {
        color: #fff;
        text-decoration: none;
        margin-left: 15px;
        font-size: 14px;
    }
    .nav a:hover {
        text-decoration: underline;
    }
    .welcome {
        font-size: 14px;
        margin-right: 15px;
    }
    .content {
        padding: 40px;
    }
</style>
</head>

<body>

<!-- 상단 헤더 -->
<div class="header">
    <div class="logo">HOME</div>

    <div class="nav">
        <!-- 로그인 전 -->
        <c:if test="${session_id == null}">
            <a href="./login.do">로그인</a>
            <a href="./agree.do">회원가입</a>
        </c:if>

        <!-- 로그인 후 -->
        <c:if test="${session_id != null}">
            <span class="welcome">${session_id}님 환영합니다</span>
            <a href="./board.do">게시판</a>
            <a href="./member.do">회원정보</a>
            <a href="./logout.do">로그아웃</a>
        </c:if>
    </div>
</div>

<!-- 본문 -->
<div class="content">
    <h2>메인페이지</h2>

    <c:if test="${session_id == null}">
        <h3>로그인을 하셔야 글쓰기가 가능합니다.</h3>
    </c:if>

    <c:if test="${session_id != null}">
        <h3>로그인 후 글쓰기가 가능합니다.</h3>
    </c:if>
</div>

</body>
</html>
