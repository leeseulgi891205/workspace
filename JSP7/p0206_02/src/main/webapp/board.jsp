<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
	String sessionId = (String) session.getAttribute("sessionId");
	String sessionName = (String) session.getAttribute("sessionName");
%>
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>VLAST Shop - 게시판</title>
</head>
<body>
	<!-- Header -->
	<div style="display: flex; justify-content: space-between; align-items: center; padding: 0 40px; height: 60px; border-bottom: 1px solid #f0f0f0;">
		<h2 style="margin: 0; color: #035fe0;">VLAST Shop</h2>
		<div style="display: flex; gap: 15px; font-size: 13px;">
			<% if (sessionId != null) { %>
				<span><strong><%= sessionName %></strong>님 환영합니다!</span>
				<a href="logout.do" style="text-decoration: none; color: #636363;">로그아웃</a>
			<% } else { %>
				<a href="login.do" style="text-decoration: none; color: #636363;">로그인</a>
				<a href="membership.do" style="text-decoration: none; color: #636363;">회원가입</a>
			<% } %>
			<a href="main.do" style="text-decoration: none; color: #636363;">HOME</a>
		</div>
	</div>

	<!-- Board List -->
	<div style="max-width: 1000px; margin: 80px auto; padding: 0 20px;">
		<div style="font-size: 28px; font-weight: bold; margin-bottom: 20px; text-align: center;">공지사항</div>
		
		<table style="width: 100%; border-collapse: collapse; font-size: 14px;">
			<thead>
				<tr>
					<th style="border-bottom: 1px solid #e0e0e0; border-top: 1px solid #848484; padding: 12px 10px; text-align: left; background-color: #f9f9f9; font-weight: 600;">번호</th>
					<th style="border-bottom: 1px solid #e0e0e0; border-top: 1px solid #848484; padding: 12px 10px; text-align: left; background-color: #f9f9f9; font-weight: 600;">제목</th>
					<th style="border-bottom: 1px solid #e0e0e0; border-top: 1px solid #848484; padding: 12px 10px; text-align: left; background-color: #f9f9f9; font-weight: 600;">작성자</th>
					<th style="border-bottom: 1px solid #e0e0e0; border-top: 1px solid #848484; padding: 12px 10px; text-align: left; background-color: #f9f9f9; font-weight: 600;">작성일</th>
					<th style="border-bottom: 1px solid #e0e0e0; border-top: 1px solid #848484; padding: 12px 10px; text-align: left; background-color: #f9f9f9; font-weight: 600;">조회수</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">5</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;"><a href="#" style="color: #1a1a1a; text-decoration: none;">[공지] 추석 연휴 배송 안내</a></td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">관리자</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">2026-02-06</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">123</td>
				</tr>
				<tr>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">4</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;"><a href="#" style="color: #1a1a1a; text-decoration: none;">2월 신규 회원 이벤트 안내</a></td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">운영팀</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">2026-02-01</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">98</td>
				</tr>
				<tr>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">3</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;"><a href="#" style="color: #1a1a1a; text-decoration: none;">[점검] 사이트 정기 점검 안내</a></td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">관리자</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">2026-01-28</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">211</td>
				</tr>
				<tr>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">2</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;"><a href="#" style="color: #1a1a1a; text-decoration: none;">배송비 정책 변경 안내</a></td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">관리자</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">2026-01-20</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">156</td>
				</tr>
				<tr>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">1</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;"><a href="#" style="color: #1a1a1a; text-decoration: none;">홈페이지 리뉴얼 오픈!</a></td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left;">운영팀</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">2026-01-10</td>
					<td style="border-bottom: 1px solid #e0e0e0; padding: 12px 10px; text-align: left; color: #888; font-size: 13px;">324</td>
				</tr>
			</tbody>
		</table>

		<!-- Pagination & Search -->
		<div style="margin-top: 30px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
			<div style="display: flex; gap: 5px; justify-content: center;">
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px;">&laquo;</a>
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px; background-color: #035fe0; color: white; border-color: #035fe0;">1</a>
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px;">2</a>
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px;">3</a>
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px;">4</a>
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px;">5</a>
				<a href="#" style="padding: 6px 12px; text-decoration: none; border: 1px solid #ccc; color: #333; font-size: 13px; border-radius: 3px;">&raquo;</a>
			</div>
			<div style="display: flex; gap: 5px; justify-content: center;">
				<input type="text" placeholder="검색어 입력" style="padding: 6px 10px; border: 1px solid #ccc; border-radius: 3px; font-size: 13px;">
				<button style="padding: 6px 12px; background-color: #035fe0; color: white; border: none; border-radius: 3px; font-size: 13px; cursor: pointer;">검색</button>
			</div>
		</div>
	</div>

	<!-- Footer -->
	<footer style="border-top: 1px solid #ccc; padding: 30px; text-align: center; font-size: 13px; color: #A0A0A0; margin-top: 50px;">
		Copyright © VLAST Shop. All rights reserved.
	</footer>
</body>
</html>
