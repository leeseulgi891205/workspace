<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>form</title>
</head>
<body>
	<%
		// 세션추가
		session.setAttribute("session_id","aaa");
		// 쿠키추가 - 로컬유저컴퓨터
		Cookie cookie = new Cookie("cookie_id","cookie_bbb");
		cookie.setMaxAge(60*60); // 1시간 = 60초*60분
		response.addCookie(cookie);
	
	
	
	%>


	<h2>폼</h2>
	<from action="./formOk.jsp" method="post" name="frm">
	<input type="text" name="name" placeholder="제목을 입력하세요."><br>
	<input type="text" name="age" placeholder="이름을 입력하세요."><br>
	<input type="submit" value="전송">
</body>
</html>