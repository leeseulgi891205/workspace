<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>VLAST Shop - 로그인</title>
</head>
<body>
	<!-- Header -->
	<div style="display: flex; justify-content: space-between; align-items: center; padding: 0 40px; height: 60px; border-bottom: 1px solid #f0f0f0;">
		<h2 style="margin: 0; color: #035fe0;">VLAST Shop</h2>
		<div style="display: flex; gap: 15px; font-size: 13px;">
			<a href="membership.do" style="text-decoration: none; color: #636363;">회원가입</a> |
			<a href="main.do" style="text-decoration: none; color: #636363;">HOME</a>
		</div>
	</div>

	<!-- Login Container -->
	<div style="max-width: 1230px; margin: 0 auto; display: flex; justify-content: center; padding: 80px 0;">
		<div style="width: 320px; text-align: center;">
			<h1 style="font-size: 20px; font-weight: 700; margin-bottom: 20px; color: #1a1a1a;">로그인</h1>
			
			<% 
				String loginError = (String) request.getAttribute("loginError");
				if (loginError != null) {
			%>
				<div style="color: red; text-align: center; margin-bottom: 15px; font-size: 14px;">
					<%= loginError %>
				</div>
			<% } %>
			
			<form action="dologin.do" method="post">
				<input type="text" name="id" placeholder="아이디" style="width: 100%; padding: 12px; margin: 5px 0; border: 1px solid #ccc; font-size: 14px; height: 40px; box-sizing: border-box;" required>
				<input type="password" name="pw" placeholder="비밀번호" style="width: 100%; padding: 12px; margin: 5px 0; border: 1px solid #ccc; font-size: 14px; height: 40px; box-sizing: border-box;" required>
				<button type="submit" style="width: 100%; height: 42px; font-size: 15px; font-weight: 500; margin: 15px 0; cursor: pointer; border: none; background-color: #035fe0; color: #fafafa;">로그인</button>
			</form>
			
			<div style="margin: 15px 0; font-size: 13px;">
				<a href="#" style="text-decoration: none; color: #636363; margin: 0 5px;">아이디 찾기</a> |
				<a href="#" style="text-decoration: none; color: #636363; margin: 0 5px;">비밀번호 찾기</a>
			</div>
			
			<div style="border: 1px solid #ccc; padding: 20px; margin-top: 30px; text-align: center;">
				<p style="font-size: 13px; font-weight: 400; color: #636363; margin: 7px 0;">
					<strong style="color: #1a1a1a; font-weight: 700;">아직 회원이 아니신가요?</strong>
				</p>
				<p style="font-size: 13px; font-weight: 400; color: #636363; margin: 7px 0;">
					지금 회원가입을 하시면<br>다양하고 특별한 혜택이 준비되어 있습니다.
				</p>
				<button onclick="location.href='membership.do';" style="background-color: #fafafa; border: 1px solid #ccc; color: #1a1a1a; width: 140px; height: 45px; margin-top: 15px; cursor: pointer; font-size: 14px; font-weight: 500;">회원가입</button>
			</div>
		</div>
	</div>

	<!-- Footer -->
	<footer style="border-top: 1px solid #ccc; padding: 30px; text-align: center; font-size: 13px; color: #A0A0A0; margin-top: 50px;">
		Copyright © VLAST Shop. All rights reserved.
	</footer>
</body>
</html>
