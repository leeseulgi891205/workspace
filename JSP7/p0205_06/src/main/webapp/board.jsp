<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>게시판</title>
	<style>
		body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
		.container { max-width: 1000px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 5px; }
		h2 { text-align: center; color: #333; margin-bottom: 30px; }
		.board-controls { text-align: right; margin-bottom: 20px; }
		a.btn { 
			display: inline-block;
			padding: 10px 20px;
			background-color: #0066cc;
			color: white;
			text-decoration: none;
			border-radius: 3px;
			margin: 5px;
		}
		a.btn:hover { background-color: #0052a3; }
		table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
		th { background-color: #0066cc; color: white; padding: 12px; text-align: center; }
		td { padding: 12px; border-bottom: 1px solid #ddd; }
		tr:hover { background-color: #f9f9f9; }
		.board-title { text-align: left; }
		.board-title a { color: #0066cc; text-decoration: none; }
		.board-title a:hover { text-decoration: underline; }
		.board-author, .board-date, .board-views { text-align: center; }
		.no-data { text-align: center; padding: 40px; color: #999; }
		.pagination { text-align: center; margin-top: 20px; }
		.pagination a { display: inline-block; padding: 5px 10px; margin: 0 3px; background-color: #ddd; color: #333; text-decoration: none; border-radius: 3px; }
		.pagination a:hover { background-color: #0066cc; color: white; }
		.nav-link { text-align: center; margin-top: 20px; }
		.nav-link a { display: inline-block; padding: 8px 15px; background-color: #999; color: white; text-decoration: none; border-radius: 3px; margin: 0 5px; }
		.nav-link a:hover { background-color: #666; }
	</style>
</head>
<body>
	<div class="container">
		<h2>게시판</h2>
		
		<div class="board-controls">
			<a href="writeForm.do" class="btn">글작성</a>
		</div>
		
		<table>
			<tr>
				<th style="width: 60px;">번호</th>
				<th style="width: 500px;">제목</th>
				<th style="width: 100px;">작성자</th>
				<th style="width: 150px;">작성일</th>
				<th style="width: 80px;">조회</th>
			</tr>
			<c:if test="${empty boardList}">
				<tr>
					<td colspan="5" class="no-data">게시글이 없습니다.</td>
				</tr>
			</c:if>
			<c:if test="${not empty boardList}">
				<c:forEach var="board" items="${boardList}" varStatus="status">
					<tr>
						<td class="board-views">${board.no}</td>
						<td class="board-title">
							<a href="boardView.do?no=${board.no}">${board.title}</a>
						</td>
						<td class="board-author">${board.writer}</td>
						<td class="board-date">${board.writeDate}</td>
						<td class="board-views">${board.views}</td>
					</tr>
				</c:forEach>
			</c:if>
		</table>
		
		<div class="pagination">
			<a href="#">◀ 이전</a>
			<a href="#">1</a>
			<a href="#">2</a>
			<a href="#">3</a>
			<a href="#">다음 ▶</a>
		</div>
		
		<div class="nav-link">
			<a href="main.do">메인페이지</a>
		</div>
	</div>
</body>
</html>
