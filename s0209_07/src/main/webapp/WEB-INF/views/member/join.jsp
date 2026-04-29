<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>회원가입</title>
</head>
<body>
    <h2>회원가입</h2>
    <form action="/member/join" method="post">
        아이디: <input type="text" name="id" required>
        <br>
        이름: <input type="text" name="name">
        <br>
        비밀번호: <input type="password" name="password" required><br>
        
        <button type="submit">가입완료</button>
    </form>
</body>
</html>