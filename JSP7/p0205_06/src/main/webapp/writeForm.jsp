<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>게시글 작성</title>
	<style>
	body{margin:0;padding:40px; font-family:Arial,sans-serif; background:#fafafa;}
	.container{max-width:820px; margin:0 auto; background:#fff;
	padding:32px;border:1px solid #ddd;}
	h2{text-align:center; color:#222;margin-bottom:40px;
	font-size:22px; letter-spacing:-0.5px;}
	form{display:flex; flex-direction:column;}
	.form-group{margin-bottom:20px;}
	label{font-weight:600; color:#333; margin-bottom:8px; display:block;}
	input[type="text"],textarea,select{
	width:100%; padding:12px; border:1px solid #ccc;
	font-size:14px; box-sizing:border-box;}
	textarea{min-height:280px; resize:vertical;}
	input:focus,textarea:focus,select:focus{
	outline:none; border-color:#000;}
	.btn-group{display:flex; gap:12px;margin-top:30px;}
	button{flex:1;padding:14px; border:1px solid #000;
	background:#fff; font-size:15px; font-weight:600; cursor:pointer;}
	button[type="submit"]:hover{
	background:#000; color:#fff;}
	button[type="reset"]:hover{
	background:#f0f0f0;}
	.nav-link{text-align:center; margin-top:30px;}
	.nav-link a{
	display:inline-block; padding:10px 18px;
	border:1px solid #000; color:#000;
	text-decoration:none; font-size:14px;}
	.nav-link a:hover{background:#000; color:#fff;}
	</style>

</head>
<body>
	<div class="container">
		<h2>게시글 작성</h2>
		
		<form action="writeOk.do" method="post">
			<div class="form-group">
				<label for="writer">작성자:</label>
				<input type="text" id="writer" name="writer" placeholder="작성자명을 입력하세요" required autofocus>
			</div>
			
			<div class="form-group">
				<label for="pwd">비밀번호:</label>
				<input type="text" id="pwd" name="pwd" placeholder="게시글 수정/삭제 시 필요한 비밀번호" required>
			</div>
			
			<div class="form-group">
				<label for="title">제목:</label>
				<input type="text" id="title" name="title" placeholder="게시글의 제목을 입력하세요" required>
			</div>
			
			<div class="form-group">
				<label for="content">내용:</label>
				<textarea id="content" name="content" placeholder="게시글의 내용을 입력하세요" required></textarea>
			</div>
			
			<div class="btn-group">
				<button type="submit">작성</button>
				<button type="reset">초기화</button>
			</div>
		</form>
		
		<div class="nav-link">
			<a href="login.do">게시판으로 돌아가기</a>
		</div>
	</div>
</body>
</html>
