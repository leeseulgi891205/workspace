<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
<h2>로그인</h2>

<form action="/login" method="post">
    아이디: <input type="text" name="id"><br>
    비밀번호: <input type="password" name="pw"><br>
    <button type="submit">로그인</button>
</form>

</body>
</html>
