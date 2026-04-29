<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>게시글 작성</title>
</head>
<body>
<h2>게시글 작성</h2>
<form action="board" method="post">
    <label>아이디</label><br>
    <input type="text" name="id" placeholder="아이디를 입력하세요"><br>
    <label>글 번호</label><br>
    <input type="text" name="bno" placeholder="번호를 입력하세요."><br>
    <label>제목</label><br>
    <input type="text" name="btitle" placeholder="제목을 입력하세요."><br>
    <label>내용</label><br>
    <textarea name="bcontent" rows="5" cols="30" placeholder="내용을 입력하세요."></textarea><br>
    <input type="submit" value="등록">
</form>
<ul>
    <li><a href="/">홈으로</a></li>
</ul>
</body>
</html>
