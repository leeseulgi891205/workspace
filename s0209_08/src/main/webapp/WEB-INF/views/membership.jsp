<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>회원가입</title>
	</head>
	<body>
		<h2>회원가입</h2>
		<form action="/member/membershipOk" method="post" name="frm">
			<input type="text" name="id" placeholder="아이디를 입력하세요."><br>
			<input type="text" name="pw" placeholder="비밀번호를 입력하세요."><br>
			<input type="text" name="name" placeholder="이름을 입력하세요."><br>
			<input type="text" name="phone" placeholder="전화번호를 입력하세요."><br>
			<input type="email" name="email" placeholder="이메일을 입력하세요."><br>
			<!-- 추가: 성별 체크박스 (name="gender") -->
			<label>성별</label><br>
			<label><input type="checkbox" name="gender" value="남자"> 남자</label>
			<label><input type="checkbox" name="gender" value="여자"> 여자</label>
			<br>
			<!-- 추가: 관심사 체크박스 (name="hobby" - 다중 선택 가능) -->
			<label>관심사</label><br>
			<label><input type="checkbox" name="hobby" value="스포츠"> 스포츠</label>
			<label><input type="checkbox" name="hobby" value="음악"> 음악</label>
			<label><input type="checkbox" name="hobby" value="독서"> 독서</label>
			<label><input type="checkbox" name="hobby" value="영화"> 영화</label>
			<br>
			<input type="submit" value="회원가입">
		</form>
	</body>
</html>