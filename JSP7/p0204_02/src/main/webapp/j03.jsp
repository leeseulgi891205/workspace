<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>파일업로드</title>
</head>
<body>
	<h2>파일업로드</h2>
	<form action="./fileOk.jsp" method="post" enctype="frm" enctype="multipart/form-data">
    <input type="text" name="title" placeholder="제목을 입력하세요.">
    <br>
    <input type="file" value="bfile"><br>
    <input type="submit" value="전송">
	
	
</body>
</html>