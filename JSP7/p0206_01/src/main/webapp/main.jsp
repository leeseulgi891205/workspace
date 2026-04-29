<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
	String sessionId = (String) session.getAttribute("sessionId");
	String sessionName = (String) session.getAttribute("sessionName");
%>
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>메인페이지</title>
	<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛍️</text></svg>">
	<style>
		* {
			margin: 0;
			padding: 0;
			box-sizing: border-box;
		}
		body {
			font-family: 'Arial', sans-serif;
			background: #fff;
			color: #1a1a1a;
		}
		.header {
			width: 100%;
			height: 60px;
			display: flex;
			justify-content: space-between;
			align-items: center;
			padding: 0 40px;
			border-bottom: 1px solid #f0f0f0;
			background: #fff;
		}
		.header h3 {
			font-size: 20px;
			font-weight: 700;
			color: #035fe0;
		}
		.top-menu {
			display: flex;
			gap: 20px;
			font-size: 14px;
			align-items: center;
		}
		.top-menu span {
			color: #636363;
		}
		.top-menu a {
			text-decoration: none;
			color: #035fe0;
			font-weight: 500;
			cursor: pointer;
		}
		.top-menu a:hover {
			text-decoration: underline;
			color: #0247a8;
		}
		.container {
			max-width: 1200px;
			margin: 0 auto;
			padding: 40px 20px;
		}
		h2 {
			text-align: center;
			color: #035fe0;
			margin-bottom: 30px;
			font-size: 28px;
		}
		.welcome {
			background-color: #f0f8ff;
			border: 1px solid #035fe0;
			padding: 20px;
			border-radius: 8px;
			margin-bottom: 30px;
			text-align: center;
			font-size: 16px;
		}
		.welcome strong {
			color: #035fe0;
			font-size: 18px;
		}
		ul {
			list-style: none;
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
			gap: 15px;
		}
		li {
			padding: 0;
		}
		li a {
			display: block;
			padding: 15px 20px;
			border: 1px solid #ccc;
			border-radius: 6px;
			text-decoration: none;
			color: #035fe0;
			font-size: 16px;
			font-weight: 500;
			text-align: center;
			transition: all 0.3s ease;
		}
		li a:hover {
			background-color: #035fe0;
			color: #fff;
			border-color: #035fe0;
			transform: translateY(-2px);
			box-shadow: 0 4px 8px rgba(3, 95, 224, 0.2);
		}
	</style></head>
<body>
	<div class="header">
		<h3 style="margin: 0;">VLAST Shop</h3>
		<div class="top-menu">
			<% if (sessionId != null) { %>
				<span><strong><%= sessionName %></strong>님 환영합니다!</span>
				<a href="logout.do">로그아웃</a>
			<% } else { %>
				<a href="login.do">로그인</a>
				<a href="membership.do">회원가입</a>
			<% } %>
		</div>
	</div>

	<div class="container">
		<h2>홈페이지에 오신걸 환영합니다.</h2>
		
		<% if (sessionId != null) { %>
			<!-- 로그인 후 -->
			<div class="welcome">
				<strong><%= sessionName %></strong>님, 환영합니다! (ID: <%= sessionId %>)
			</div>
			<ul>
				<li><a href="member.do">전체회원정보</a></li>
				<li><a href="board.do">게시판정보</a></li>
				<li><a href="logout.do">로그아웃</a></li>
			</ul>
		<% } else { %>
			<!-- 로그인 전 -->
			<ul>
				<li><a href="login.do">로그인</a></li>
				<li><a href="membership.do">회원가입</a></li>
				<li><a href="board.do">게시판정보</a></li>
			</ul>
		<% } %>
	</div>
</body>
</html>