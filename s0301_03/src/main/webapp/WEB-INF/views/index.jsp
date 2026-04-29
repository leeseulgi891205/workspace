<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>메인페이지</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        a { cursor: pointer; }

        .navbar {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 18px 40px;
            background-color: white;
            border-bottom: 1px solid #ddd;
        }

        .nav-center a {
            margin: 0 25px;
            text-decoration: none;
            color: black;
            font-size: 18px;
            font-weight: 500;
        }

        .nav-center a:hover {
            color: #555;
        }

        .nav-right {
            position: absolute;
            right: 40px;
            display: flex;
            align-items: center;
            gap: 15px;
            font-size: 14px;
            color: black;
        }

        .nav-right a {
            text-decoration: none;
            color: black;
            font-weight: 500;
        }

        .nav-right a:hover {
            color: #555;
        }

        .container {
            padding: 40px;
            text-align: center;
        }
    </style>

    <script>
        function logoutBtn(){
            alert("로그아웃 되었습니다.");
            location.href="/member/logout";
        }
    </script>
</head>

<body>

    <nav class="navbar">

        <!-- 가운데 메뉴 -->
        <div class="nav-center">
            <a href="/">HOME</a>
            <a href="/board/blist">게시판</a>
            <c:if test="${session_id != null}">
                <a href="/member/mlist">회원리스트</a>
            </c:if>
        </div>

        <!-- 오른쪽 로그인 영역 -->
        <div class="nav-right">

            <c:if test="${session_id == null}">
                <a href="/member/login">로그인</a>
                <a href="/member/memberShip">회원가입</a>
            </c:if>

            <c:if test="${session_id != null}">
                <span><b>${session_id}</b>님 환영합니다</span>
                <a onclick="logoutBtn()">로그아웃</a>
            </c:if>

        </div>
    </nav>

    <div class="container">

    </div>

</body>
</html>
