<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>폼</title>
	</head>
	<body>
	  <%
	     request.setAttribute("nickName", "길동스");
	  %>
	  <h2>form 페이지</h2>
	  <h3>request nickName : ${nickName }</h3>
	  <%
	    // sendRedirect 페이지 이동가능 - request,response reset
	    //response.sendRedirect("./formOk.jsp");	     
	    // RequestDispatcher 페이지 이동가능 - request,response 추가해서 보냄.
	    RequestDispatcher dispatcher = request.getRequestDispatcher("./formOk.jsp");
	    dispatcher.forward(request, response);
	  %>
	  <form action="./formOk.jsp" method="post" name="frm">
	    <input type="text" name="id" placeholder="아이디"><br>
	    <input type="text" name="pw" placeholder="패스워드"><br>
	    <input type="text" name="name" placeholder="이름"><br>
	    <input type="text" name="phone" placeholder="전화번호"><br>
	    <input type="text" name="email" placeholder="이메일"><br>
	    <input type="text" name="gender" placeholder="성별"><br>
	    <input type="text" name="hobby" placeholder="취미"><br>
	    <input type="submit" value="전송">
	  </form>
	
	</body>
</html>