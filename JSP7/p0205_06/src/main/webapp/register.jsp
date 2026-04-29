<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>회원가입</title>
	<style>
		body { font-family: Arial, sans-serif; padding: 20px; }
		h2 { text-align: center; color: #333; }
		.container { max-width: 400px; margin: 30px auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
		form { display: flex; flex-direction: column; }
		label { margin-top: 10px; font-weight: bold; color: #333; }
		input[type="text"], input[type="password"], input[type="email"], input[type="tel"], select, textarea {
			margin-top: 5px;
			padding: 8px;
			border: 1px solid #bbb;
			border-radius: 3px;
			font-size: 14px;
		}
		input[type="radio"], input[type="checkbox"] {
			margin-right: 5px;
		}
		.form-group { margin-bottom: 15px; }
		.gender-group, .hobby-group { margin-top: 5px; }
		button { 
			margin-top: 20px; 
			padding: 10px; 
			background-color: #0066cc; 
			color: white; 
			border: none; 
			border-radius: 3px; 
			cursor: pointer;
			font-size: 16px;
		}
		button:hover { background-color: rgb(0, 0, 0); }
		a { color: rgb(0, 0, 0); text-decoration: none; }
		a:hover { text-decoration: underline; }
		.btn-group { display: flex; gap: 10px; }
		button[type="reset"] { background-color: #999; }
		button[type="reset"]:hover { background-color: #777; }
	</style>
</head>
<body>
	<h2>회원가입</h2>
	<div class="container">
		<form action="registerOk.do" method="post">
			<div class="form-group">
				<label for="id">아이디:</label>
				<input type="text" id="id" name="id" required>
			</div>
			
			<div class="form-group">
				<label for="pw">패스워드:</label>
				<input type="password" id="pw" name="pw" required>
			</div>
			
			<div class="form-group">
				<label for="name">이름:</label>
				<input type="text" id="name" name="name" required>
			</div>
			
			<div class="form-group">
				<label for="phone">전화번호:</label>
				<input type="tel" id="phone" name="phone" placeholder="010-1234-5678" required>
			</div>
			
			<div class="form-group">
				<label for="email">이메일:</label>
				<input type="email" id="email" name="email" required>
			</div>
			
			<div class="form-group">
				<label>성별:</label>
				<div class="gender-group">
					<input type="radio" id="male" name="gender" value="남자" required>
					<label for="male" style="margin: 0;">남자</label>
					
					<input type="radio" id="female" name="gender" value="여자" style="margin-left: 20px;">
					<label for="female" style="margin: 0;">여자</label>
				</div>
			</div>
			
			<div class="form-group">
				<label>취미:</label>
				<div class="hobby-group">
					<input type="checkbox" id="hobby1" name="hobby" value="게임">
					<label for="hobby1" style="margin: 0;">게임</label>
					
					<input type="checkbox" id="hobby2" name="hobby" value="영화" style="margin-left: 20px;">
					<label for="hobby2" style="margin: 0;">영화</label>
					
					<input type="checkbox" id="hobby3" name="hobby" value="음악" style="margin-left: 20px;">
					<label for="hobby3" style="margin: 0;">음악</label>
				</div>
			</div>
			
			<div class="btn-group">
				<button type="submit">가입</button>
				<button type="reset">초기화</button>
			</div>
		</form>
		<p style="text-align: center; margin-top: 20px;">
			<a href="main.do">메인페이지로 돌아가기</a>
		</p>
	</div>
</body>
</html>
