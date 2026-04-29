<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VLAST Shop - 회원가입</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 0;
      padding: 0;
      background: #fff;
      color: #1a1a1a;
    }
    /* Header */
    .header {
      width: 100%;
      height: 60px;
      display: flex;
      justify-content: flex-end;
      align-items: center;
      padding: 0 40px;
      box-sizing: border-box;
      border-bottom: 1px solid #f0f0f0;
    }
    .top-menu {
      display: flex;
      gap: 15px;
      font-size: 13px;
      color: #636363;
      margin-right: 20px;
    }
    .top-menu a {
      text-decoration: none;
      color: #636363;
    }
    .top-menu a:hover {
      color: #035fe0;
    }

    .signup-container {
      max-width: 500px;
      margin: 50px auto;
      padding: 0 20px;
      box-sizing: border-box;
    }
    .signup-title {
      font-size: 28px;
      font-weight: bold;
      margin-bottom: 30px;
      text-align: center;
    }

    form.signup-form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }

    .form-group {
      display: flex;
      flex-direction: column;
    }

    .form-group label {
      font-size: 14px;
      font-weight: bold;
      margin-bottom: 5px;
      color: #1a1a1a;
    }

    .form-group input[type="text"],
    .form-group input[type="password"],
    .form-group input[type="email"],
    .form-group input[type="tel"],
    .form-group select {
      padding: 10px;
      font-size: 14px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }

    .form-group input:focus,
    .form-group select:focus {
      outline: none;
      border-color: #035fe0;
      background-color: #f9f9f9;
    }

    .form-group-inline {
      display: flex;
      gap: 10px;
    }

    .form-group-inline input {
      flex: 1;
      padding: 10px;
      font-size: 14px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .radio-group, .checkbox-group {
      display: flex;
      gap: 20px;
      margin-top: 5px;
    }

    .radio-group label, .checkbox-group label {
      display: flex;
      align-items: center;
      gap: 5px;
      font-weight: normal;
      margin: 0;
    }

    .radio-group input, .checkbox-group input {
      cursor: pointer;
    }

    .form-buttons {
      display: flex;
      justify-content: center;
      gap: 15px;
      margin-top: 20px;
    }

    .form-buttons button {
      padding: 12px 40px;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      color: white;
      background-color: #035fe0;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    .form-buttons button:hover {
      background-color: #0046b3;
    }

    .form-buttons .cancel {
      background-color: #6c757d;
    }

    .form-buttons .cancel:hover {
      background-color: #5a6268;
    }

    footer {
      border-top: 1px solid #ccc;
      padding: 30px;
      text-align: center;
      font-size: 13px;
      color: #A0A0A0;
      margin-top: 50px;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <div class="header">
    <div class="top-menu">
      <a href="./login.do">로그인</a> |
      <a href="./agree.do">회원가입</a> |
      <a href="#">주문조회</a> |
      <a href="${pageContext.request.contextPath}/">홈으로</a>
    </div>
  </div>

  <!-- 회원가입 폼 -->
  <div class="signup-container">
    <div class="signup-title">회원가입</div>
    
    <!-- 단계 표시 추가 -->
    <div style="text-align: center; padding-bottom: 30px; border-bottom: 1px solid #ccc; margin-bottom: 30px;">
      <ul style="display: flex; justify-content: center; gap: 40px; list-style: none; padding: 0; margin: 0;">
        <li style="font-size: 14px;">1. 약관동의</li>
        <li style="font-size: 15px; color: #035fe0; font-weight: bold;">2. 정보입력</li>
        <li style="font-size: 14px;">3. 가입완료</li>
      </ul>
    </div>
    
    <form action="./doMembership.do" method="post" class="signup-form" id="signupForm">
      
      <div class="form-group">
        <label for="id">아이디 *</label>
        <input type="text" name="id" id="id" placeholder="아이디" maxlength="20" required />
      </div>

      <div class="form-group">
        <label for="pw">비밀번호 *</label>
        <input type="password" name="pw" id="pw" placeholder="비밀번호" maxlength="20" required />
      </div>

      <div class="form-group">
        <label for="pw2">비밀번호 확인 *</label>
        <input type="password" name="pw2" id="pw2" placeholder="비밀번호 확인" maxlength="20" required />
      </div>

      <div class="form-group">
        <label for="name">이름 *</label>
        <input type="text" name="name" id="name" placeholder="이름" maxlength="20" required />
      </div>

      <div class="form-group">
        <label>휴대폰 *</label>
        <div class="form-group-inline">
          <input type="tel" name="phone1" placeholder="010" maxlength="3" required />
          <input type="tel" name="phone2" placeholder="0000" maxlength="4" required />
          <input type="tel" name="phone3" placeholder="0000" maxlength="4" required />
        </div>
      </div>

      <div class="form-group">
        <label for="email">이메일</label>
        <input type="email" name="email" id="email" placeholder="example@email.com" maxlength="50" />
      </div>

      <div class="form-group">
        <label>성별</label>
        <div class="radio-group">
          <label><input type="radio" name="gender" value="M" /> 남성</label>
          <label><input type="radio" name="gender" value="F" /> 여성</label>
        </div>
      </div>

      <div class="form-group">
        <label>관심사</label>
        <div class="checkbox-group">
          <label><input type="checkbox" name="hobby" value="독서" /> 독서</label>
          <label><input type="checkbox" name="hobby" value="영화" /> 영화</label>
          <label><input type="checkbox" name="hobby" value="스포츠" /> 스포츠</label>
          <label><input type="checkbox" name="hobby" value="게임" /> 게임</label>
        </div>
      </div>

      <div class="form-buttons">
        <button type="submit">가입하기</button>
        <button type="button" class="cancel" onclick="history.back()">취소</button>
      </div>
    </form>
  </div>

  <!-- Footer -->
  <footer>
    Copyright © VLAST Shop. All rights reserved.
  </footer>

  <script>
    const signupForm = document.getElementById('signupForm');

    signupForm.addEventListener('submit', (e) => {
      const pw = document.getElementById('pw').value.trim();
      const pw2 = document.getElementById('pw2').value.trim();

      if (pw !== pw2) {
        e.preventDefault();
        alert('비밀번호가 일치하지 않습니다.');
        return;
      }
    });
  </script>
</body>
</html>
