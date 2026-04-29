<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Insert title here</title>
	</head>
	<body>
	<script>
		if(${flag == null}){ //board 인설트 성공
			alert("게시글이 저장되었습니다.");
			location.href="./board.do";

		}else if(${flag == 2}){ //board 인설트 실패
            alert("게시글이 삭제되었습니다.");
            location.href="./board.do"
         
        }else if(${flag == 3}){
        	alert("게시글이 수정되었습니다.")
        	location.href="./board.do"
        }
	</script>
	
	</body>
</html>