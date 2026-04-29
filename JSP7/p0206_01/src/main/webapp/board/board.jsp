<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%><!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>게시판</title>
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
      text-align: center;
      font-weight: 600;
    }
    td {
      padding: 12px;
      text-align: center;
    }
    td:nth-child(2) {
      text-align: left;
    }
    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
    tr:hover {
      background-color: #f0f8ff;
    }
    a {
      color: #035fe0;
      text-decoration: none;
      font-weight: 500;
    }
    a:hover {
      text-decoration: underline;
      color: #0247a8;
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
    <h1>게시판</h1>
    <table>
      <thead>
        <tr>
          <th style="width: 60px;">번호</th>
          <th>제목</th>
          <th style="width: 100px;">작성자</th>
          <th style="width: 120px;">작성일</th>
          <th style="width: 80px;">조회수</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>5</td>
          <td><a href="#">시스템 점검 안내</a></td>
          <td>관리자</td>
          <td>2026-02-06</td>
          <td>320</td>
        </tr>
        <tr>
          <td>4</td>
          <td><a href="#">2월 신상품 입고 완료</a></td>
          <td>staff</td>
          <td>2026-02-05</td>
          <td>245</td>
        </tr>
        <tr>
          <td>3</td>
          <td><a href="#">배송 정책 변경 안내</a></td>
          <td>관리자</td>
          <td>2026-02-01</td>
          <td>180</td>
        </tr>
        <tr>
          <td>2</td>
          <td><a href="#">고객 만족도 조사 이벤트</a></td>
          <td>marketing</td>
          <td>2026-01-28</td>
          <td>156</td>
        </tr>
        <tr>
          <td>1</td>
          <td><a href="#">환영합니다! VLAST Shop 게시판입니다</a></td>
          <td>관리자</td>
          <td>2026-01-20</td>
          <td>523</td>
        </tr>
      </tbody>
    </table>
    <button class="btn" onclick="location.href='main.do'">메인으로</button>
  </div>
</body>
</html>
