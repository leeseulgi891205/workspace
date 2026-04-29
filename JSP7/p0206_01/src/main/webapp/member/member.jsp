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
  <title>회원정보</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛍️</text></svg>">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      font-family: 'Arial', sans-serif;
      background: #fff;
      color: #1a1a1a;
    }
    .header {
      width: 100%;
      height: 60px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 40px;
      box-sizing: border-box;
      border-bottom: 1px solid #f0f0f0;
    }
    .header h3 {
      font-size: 20px;
      font-weight: 700;
      color: #035fe0;
    }
    .top-menu {
      display: flex;
      gap: 20px;
      font-size: 14px;
      align-items: center;
    }
    .top-menu span {
      color: #636363;
    }
    .top-menu a {
      text-decoration: none;
      color: #035fe0;
      font-weight: 500;
      cursor: pointer;
    }
    .top-menu a:hover {
      text-decoration: underline;
      color: #0247a8;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 20px;
    }
    h1 {
      text-align: center;
      color: #035fe0;
      margin-bottom: 30px;
      font-size: 28px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    table, th, td {
      border: 1px solid #ccc;
    }
    th {
      background-color: #035fe0;
      color: #fff;
      padding: 12px;
      text-align: left;
      font-weight: 600;
    }
    td {
      padding: 12px;
    }
    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
    tr:hover {
      background-color: #f0f8ff;
    }
    .btn {
      padding: 10px 20px;
      background-color: #035fe0;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      margin-top: 20px;
      font-weight: 500;
      transition: all 0.3s ease;
    }
    .btn:hover {
      background-color: #0247a8;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(3, 95, 224, 0.2);
    }
    .login-warning {
      background-color: #fff3cd;
      border: 1px solid #ffc107;
      padding: 15px;
      border-radius: 4px;
      text-align: center;
      margin: 20px 0;
    }
    .login-warning a {
      color: #035fe0;
      text-decoration: none;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="header">
    <h3 style="margin: 0;">VLAST Shop</h3>
    <div class="top-menu">
      <% if (sessionId != null) { %>
        <span><strong><%= sessionName %></strong>님 환영합니다!</span>
        <a href="logout.do">로그아웃</a>
      <% } else { %>
        <a href="login.do">로그인</a>
        <a href="membership.do">회원가입</a>
      <% } %>
      <a href="main.do">HOME</a>
    </div>
  </div>
  <div class="container">
    <h1>전체 회원 정보</h1>
    
    <% if (sessionId == null) { %>
      <div class="login-warning">
        로그인이 필요합니다. <a href="login.do">로그인하러 가기</a>
      </div>
    <% } %>
    
    <table>
      <thead>
        <tr>
          <th>아이디</th>
          <th>이름</th>
          <th>이메일</th>
          <th>전화번호</th>
          <th>성별</th>
          <th>취미</th>
        </tr>
      </thead>
      <tbody>
      <c:forEach var="mdto" items="${memberList}">
        <tr>
          <td>${member.id }</td>
          <td class="title"><a href="./memberView.do">${member.id }</td>
          <td>${member.phone }</td>
          <td class="date">${member.gender }</td>
          <td class="views">${member.hobby }</td>
        </tr>
        </c:forEach>
      </tbody>
    </table>
    <button class="btn" onclick="location.href='main.do'">메인으로</button>
  </div>
</body>
</html>
