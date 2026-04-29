<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>메인페이지</title>
	<style>
	body{margin:0;font-family:Arial;}
	h2{text-align:center;background:#fff;color:#000;
	margin:0;padding:20px;border-bottom:1px solid #000;}
	ul{list-style:none;margin:0;padding:0;display:flex;
	justify-content:center;background:#fff;border-bottom:1px solid #000;}
	li{padding:0;}
	a{display:block;padding:15px 30px;
	color:#000;text-decoration:none;
	transition:font-size .2s;}
	a:hover{font-size:18px;}
	</style>

</head>
<body>
	<h2>홈페이지에 오신걸 환영합니다.</h2>
	<ul>
	    <li><a href="member.do">전체회원정보</a></li>
	    <li><a href="login.do">게시판</a></li>
	    <li><a href="register.do">회원가입</a></li>
	    <li><a href="search.do">회원검색</a></li>
	</ul>
</body>
</html>