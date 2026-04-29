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
	<title>VLAST Shop - 메인</title>
</head>
<body>

	<!-- Header -->
	<div style="border-bottom: 1px solid #f0f0f0; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center;">
		<h1 style="margin: 0; color: #035fe0;"></h1>
		<div style="display: flex; gap: 20px; align-items: center;">
			<% if (sessionId != null) { %>
				<span><strong><%= sessionName %></strong>님 환영합니다!</span>
				<a href="logout.do" style="text-decoration: none; color: #035fe0;">로그아웃</a>
			<% } else { %>
				<a href="login.do" style="text-decoration: none; color: #035fe0;">로그인</a>
				<a href="membership.do" style="text-decoration: none; color: #035fe0;">회원가입</a>
			<% } %>
			<a href="board.do" style="text-decoration: none; color: #035fe0;">게시판</a>
		</div>
	</div>

	<!-- Main Content -->
	<div style="max-width: 1200px; margin: 50px auto; padding: 0 20px; text-align: center;">
		<h2 style="color: #035fe0; font-size: 28px; margin-bottom: 30px;">VLAST Shop에 오신걸 환영합니다.</h2>
		
		<% if (sessionId != null) { %>
			<!-- 로그인 후 -->
			<div style="background-color: #f0f8ff; border: 1px solid #035fe0; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
				<strong><%= sessionName %></strong>님, 환영합니다! (ID: <%= sessionId %>)
			</div>
			<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
				<div style="padding: 15px 20px; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; transition: all 0.3s ease;">
					<a href="board.do" style="text-decoration: none; color: #035fe0; display: block; font-size: 16px; font-weight: 500;">게시판정보</a>
				</div>
				<div style="padding: 15px 20px; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; transition: all 0.3s ease;">
					<a href="logout.do" style="text-decoration: none; color: #035fe0; display: block; font-size: 16px; font-weight: 500;">로그아웃</a>
				</div>
			</div>
		<% } else { %>
			<!-- 로그인 전 -->
			<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
				<div style="padding: 15px 20px; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; transition: all 0.3s ease;">
					<a href="login.do" style="text-decoration: none; color: #035fe0; display: block; font-size: 16px; font-weight: 500;">로그인</a>
				</div>
				<div style="padding: 15px 20px; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; transition: all 0.3s ease;">
					<a href="membership.do" style="text-decoration: none; color: #035fe0; display: block; font-size: 16px; font-weight: 500;">회원가입</a>
				</div>
				<div style="padding: 15px 20px; border: 1px solid #ccc; border-radius: 6px; cursor: pointer; transition: all 0.3s ease;">
					<a href="board.do" style="text-decoration: none; color: #035fe0; display: block; font-size: 16px; font-weight: 500;">게시판정보</a>
				</div>
			</div>
		<% } %>
	</div>

	<!-- Footer -->
	<footer style="border-top: 1px solid #ccc; padding: 30px; text-align: center; font-size: 13px; color: #A0A0A0; margin-top: 50px;">
		Copyright © VLAST Shop. All rights reserved.
	</footer>

</body>
</html>
