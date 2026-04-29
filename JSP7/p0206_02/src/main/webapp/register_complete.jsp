<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>회원가입 완료</title>
</head>
<body>
	<!-- Header -->
	<div style="display: flex; justify-content: space-between; align-items: center; padding: 0 40px; height: 60px; border-bottom: 1px solid #f0f0f0;">
		<h2 style="margin: 0; color: #035fe0;">VLAST Shop</h2>
		<div style="display: flex; gap: 15px; font-size: 13px;">
			<a href="login.do" style="text-decoration: none; color: #636363;">로그인</a> |
			<a href="main.do" style="text-decoration: none; color: #636363;">HOME</a>
		</div>
	</div>

	<!-- Container -->
	<div style="width: 100%; max-width: 720px; margin: 0 auto; box-sizing: border-box;">
		<!-- Title -->
		<div style="text-align: center; padding: 70px 0; font-size: 30px; font-weight: bold; color: #035fe0;">
			회원가입
		</div>
		
		<!-- Step Indicator -->
		<div style="text-align: center; padding-bottom: 20px; margin-bottom: 10px;">
			<div style="display: flex; justify-content: center; gap: 40px;">
				<div style="display: inline-block; font-size: 14px; color: #636363;">1. 약관동의</div>
				<div style="display: inline-block; font-size: 14px; color: #636363;">2. 정보입력</div>
				<div style="display: inline-block; font-size: 14px; color: #035fe0; font-weight: 700;">3. 가입완료</div>
			</div>
		</div>

		<!-- Message Box -->
		<div style="max-width: 600px; margin: 0 auto; padding: 50px 20px; border-top: 1px solid #ccc; border-bottom: 1px solid #ccc; box-sizing: border-box;">
			<p style="font-size: 24px; font-weight: 700; color: #035fe0; margin-bottom: 20px; text-align: center;">
				🎉 회원가입이 완료되었습니다!
			</p>
			<p style="font-size: 16px; color: #636363; margin-bottom: 30px; text-align: center;">
				VLAST Shop의 회원이 되신 것을 환영합니다.<br>
				로그인하여 다양한 서비스를 이용하실 수 있습니다.
			</p>
			
			<!-- Button Box -->
			<div style="display: flex; justify-content: center; gap: 15px; padding-top: 20px;">
				<button onclick="location.href='login.do';" style="width: 160px; height: 50px; font-size: 15px; font-weight: 500; border: 1px solid #035fe0; background-color: #035fe0; color: #fafafa; cursor: pointer; box-sizing: border-box; border-radius: 4px;">
					로그인하기
				</button>
				<button onclick="location.href='main.do';" style="width: 160px; height: 50px; font-size: 15px; font-weight: 400; border: 1px solid #ccc; background-color: white; color: #1a1a1a; cursor: pointer; box-sizing: border-box; border-radius: 4px;">
					메인으로
				</button>
			</div>
		</div>
	</div>

	<!-- Footer -->
	<footer style="border-top: 1px solid #ccc; padding: 30px; text-align: center; font-size: 13px; color: #A0A0A0; margin-top: 50px;">
		Copyright © VLAST Shop. All rights reserved.
	</footer>
</body>
</html>
