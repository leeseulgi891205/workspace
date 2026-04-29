<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title></title>
</head>
<body>
	<h2>결과</h2>
	<% // post방식 = setCharacterEncoding() 없으면 한글처리가 안됨.
		request.setCharacterEncoding("UTF-8");
		int i = 10;
		out.print(i+100+"<br>");
	%>
	<!-- jsp태그랑 함꼐 사용할수 없음. jstl태그를 사용하게 됨. -->
	<p>el태그 사용 : ${param.title} </p>
	<p>el태그 사용 : ${param.name} </p>
	<p>el태그 session 이름만 : ${session_id} </p>}
	<p>el태그 cookie : ${cookie.cookie_id.value} </p>}
	
	<p>el태그 session : ${sessionScope.session_id} </p>}
	<p>변수선언 i : ${i}</p> }
	
	<p>-----------------------------------------------------</p>
	
	<p>jsp request:<%= request.getParameter("title") %></p>
	<p>jsp request:<%= request.getParameter("name") %></p>
	<p>jsp 세션:<%= session.getAttribute("session_id") %></p>
	<%
		Cookie[] cookioes = request.getCookies();
		for(Cookie cookie : cookioes) {
            out.println("쿠키 : "+cookie.getName()+" = "+cookie.getValue()+"<br>");
		}
	%>
	
	<p><%= i+100 %></p>
</body>
</html>