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
		<form action="join" method="post">
			<input type="text" name="id" placeholder="아이디를 입력하세요"></input><br>
			<input type="password" name="pw" placeholder="비밀번호를 입력하세요"></input><br>
			<input type="text" name="name" placeholder="이름을 입력하세요"></input><br>
			<input type="text" name="email" placeholder="이메일을 입력하세요"></input><br>
			<input type="text" name="phone" placeholder="전화번호를 입력하세요"></input><br>
			<label>성별</label><br>
			<input type="radio" id="male" name="gender" value="남자">
            <label for="male">남자</label>
            <input type="radio" id="female" name="gender" value="여자">
            <label for="female">여자</label>
            <br>
            <label>취미</label><br>
            <input type="checkbox" id="game" name="hobby" value="게임">
            <label for="game">게임</label>
            <input type="checkbox" id="movie" name="hobby" value="영화">
            <label for="movie">영화</label>
            <input type="checkbox" id="music" name="hobby" value="음악">
            <label for="music">음악</label>
            <input type="checkbox" id="sports" name="hobby" value="운동">
            <label for="sports">운동</label>
            <input type="checkbox" id="travel" name="hobby" value="여행">
            <label for="travel">여행</label>
			<input type="submit" value="회원가입"></input>
		</form>
        <ul>
            <li><a href="/">홈으로</a></li>
            <li><a href="/login">로그인</a></li>
        </ul>
	</body>
</html>