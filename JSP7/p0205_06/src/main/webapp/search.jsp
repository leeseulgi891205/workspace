<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>회원검색</title>
	<style>
		body { font-family: Arial, sans-serif; padding: 20px; }
		h2 { text-align: center; color: #333; }
		.container { max-width: 500px; margin: 30px auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
		form { display: flex; flex-direction: column; }
		label { margin-bottom: 5px; font-weight: bold; color: #333; }
		input[type="text"] {
			padding: 10px;
			border: 1px solid #bbb;
			border-radius: 3px;
			font-size: 14px;
			margin-bottom: 20px;
		}
		.btn-group {
			display: flex;
			gap: 10px;
		}
		button { 
			padding: 10px 20px;
			background-color: #0066cc; 
			color: white; 
			border: none; 
			border-radius: 3px; 
			cursor: pointer;
			font-size: 16px;
			flex: 1;
		}
		button:hover { background-color: #0052a3; }
		button[type="reset"] { background-color: #999; }
		button[type="reset"]:hover { background-color: #777; }
		a { color: #0066cc; text-decoration: none; }
		a:hover { text-decoration: underline; }
		p { text-align: center; margin-top: 20px; }
		.search-info { 
			background-color: #f0f0f0; 
			padding: 15px; 
			border-radius: 3px; 
			margin-bottom: 20px;
		}
	</style>
</head>
<body>
	<h2>회원검색</h2>
	<div class="container">
		<div class="search-info">
			<p>검색하고 싶은 회원의 아이디를 입력하세요.</p>
		</div>
		
		<form action="searchOk.do" method="post">
			<label for="searchId">검색 아이디:</label>
			<input type="text" id="searchId" name="searchId" placeholder="검색할 아이디를 입력하세요" required autofocus>
			
			<div class="btn-group">
				<button type="submit">검색</button>
				<button type="reset">초기화</button>
			</div>
		</form>
		
		<p>
			<a href="main.do">메인페이지로 돌아가기</a>
		</p>
	</div>
</body>
</html>
