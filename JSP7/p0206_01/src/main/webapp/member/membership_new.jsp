<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>회원가입</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛍️</text></svg>">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: 'Arial', sans-serif;
      background: #f9f9f9;
      color: #1a1a1a;
    }
    
    .header {
      width: 100%;
      height: 60px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 40px;
      border-bottom: 1px solid #f0f0f0;
      background: #fff;
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
      max-width: 600px;
      margin: 40px auto;
      background: #fff;
      padding: 40px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    h1 {
      text-align: center;
      color: #035fe0;
      margin-bottom: 30px;
      font-size: 28px;
    }
    
    .form-group {
      margin-bottom: 20px;
    }
    
    label {
      display: block;
      margin-bottom: 8px;
      font-weight: 600;
      color: #1a1a1a;
    }
    
    label .required {
      color: #e74c3c;
    }
    
    input[type="text"],
    input[type="password"],
    input[type="email"],
    select {
      width: 100%;
      padding: 10px 12px;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 14px;
      font-family: 'Arial', sans-serif;
    }
    
    input[type="text"]:focus,
    input[type="password"]:focus,
    input[type="email"]:focus,
    select:focus {
      outline: none;
      border-color: #035fe0;
      box-shadow: 0 0 0 3px rgba(3, 95, 224, 0.1);
    }
    
    .input-group {
      display: flex;
      gap: 10px;
      align-items: center;
    }
    
    .input-group input {
      flex: 1;
    }
    
    .input-group button {
      padding: 10px 16px;
      background-color: #f0f0f0;
      border: 1px solid #ddd;
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px;
      font-weight: 600;
      white-space: nowrap;
      transition: all 0.3s ease;
    }
    
    .input-group button:hover {
      background-color: #035fe0;
      color: #fff;
      border-color: #035fe0;
    }
    
    .phone-input {
      display: flex;
      gap: 8px;
      align-items: center;
    }
    
    .phone-input input {
      flex: 1;
      min-width: 0;
    }
    
    .phone-input select {
      flex: 1;
      min-width: 0;
    }
    
    .phone-input span {
      color: #636363;
      font-weight: bold;
    }
    
    .btn-group {
      display: flex;
      gap: 10px;
      margin-top: 30px;
    }
    
    button[type="submit"],
    button[type="button"].cancel {
      flex: 1;
      padding: 14px;
      font-size: 16px;
      font-weight: 600;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    button[type="submit"] {
      background-color: #035fe0;
      color: #fff;
    }
    
    button[type="submit"]:hover {
      background-color: #0247a8;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(3, 95, 224, 0.2);
    }
    
    button.cancel {
      background-color: #f0f0f0;
      color: #1a1a1a;
      border: 1px solid #ddd;
    }
    
    button.cancel:hover {
      background-color: #e0e0e0;
      border-color: #999;
    }
    
    .info-text {
      font-size: 12px;
      color: #636363;
      margin-top: 8px;
    }
    
    .agreement-box {
      background-color: #f9f9f9;
      padding: 12px;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-bottom: 20px;
      max-height: 120px;
      overflow-y: auto;
      font-size: 12px;
      line-height: 1.6;
    }
    
    .checkbox-group {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 20px;
    }
    
    input[type="checkbox"] {
      width: 18px;
      height: 18px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="header">
    <h3 style="margin: 0;">VLAST Shop</h3>
    <div class="top-menu">
      <a href="login.do">로그인</a>
      <a href="main.do">HOME</a>
    </div>
  </div>
  
  <div class="container">
    <h1>회원가입</h1>
    
    <form action="domembership.do" method="post" onsubmit="return validateForm();">
      
      <!-- 약관 동의 -->
      <div class="form-group">
        <label>이용약관 및 개인정보 수집에 동의합니다 <span class="required">*</span></label>
        <div class="agreement-box">
          제1조 (목적)
          이 약관은 VLAST Shop(이하 "회사")이 제공하는 전자상거래 서비스(이하 "서비스")를 이용함에 있어 회사와 이용자의 권리, 의무 및 책임사항을 규정함을 목적으로 합니다.<br><br>
          
          제2조 (정의)
          1. "회원"이라 함은 회사의 정보를 제공받아 본 약관에 따라 회사와 이용계약을 체결한 자를 말합니다.
          2. "아이디"라 함은 회원의 식별과 서비스 이용을 위해 회원이 선정하고 회사가 승인하는 문자와 숫자의 조합을 말합니다.
        </div>
        <div class="checkbox-group">
          <input type="checkbox" id="agree" name="agree" value="Y" required>
          <label for="agree" style="margin: 0;">동의합니다</label>
        </div>
      </div>
      
      <!-- 아이디 -->
      <div class="form-group">
        <label for="id">아이디 <span class="required">*</span></label>
        <div class="input-group">
          <input type="text" id="id" name="id" placeholder="4~16자의 영문소문자, 숫자" required>
          <button type="button" onclick="checkId();">중복확인</button>
        </div>
        <div class="info-text">영문소문자, 숫자만 사용 가능하며 4자 이상 16자 이하여야 합니다.</div>
      </div>
      
      <!-- 비밀번호 -->
      <div class="form-group">
        <label for="pw">비밀번호 <span class="required">*</span></label>
        <input type="password" id="pw" name="pw" placeholder="영문,숫자,특수문자 혼합 8자 이상" required>
        <div class="info-text">영문 대소문자, 숫자, 특수문자 중 2가지 이상 조합, 8자 이상 16자 이하여야 합니다.</div>
      </div>
      
      <!-- 비밀번호 확인 -->
      <div class="form-group">
        <label for="pw_confirm">비밀번호 확인 <span class="required">*</span></label>
        <input type="password" id="pw_confirm" name="pw_confirm" placeholder="비밀번호 재입력" required>
      </div>
      
      <!-- 이름 -->
      <div class="form-group">
        <label for="name">이름 <span class="required">*</span></label>
        <input type="text" id="name" name="name" placeholder="실명입력" required>
      </div>
      
      <!-- 이메일 -->
      <div class="form-group">
        <label for="email">이메일 <span class="required">*</span></label>
        <div class="input-group">
          <input type="email" id="email" name="email" placeholder="example@domain.com" required>
          <button type="button" onclick="sendEmailCode();">인증</button>
        </div>
      </div>
      
      <!-- 인증번호 -->
      <div class="form-group">
        <label for="email_code">이메일 인증번호 <span class="required">*</span></label>
        <div class="input-group">
          <input type="text" id="email_code" name="email_code" placeholder="인증번호 입력" required>
          <button type="button" onclick="verifyEmailCode();">확인</button>
        </div>
      </div>
      
      <!-- 휴대전화 -->
      <div class="form-group">
        <label for="phone">휴대전화 <span class="required">*</span></label>
        <div class="phone-input">
          <select name="phone1" required>
            <option value="">선택</option>
            <option value="010">010</option>
            <option value="011">011</option>
            <option value="016">016</option>
            <option value="017">017</option>
            <option value="018">018</option>
            <option value="019">019</option>
          </select>
          <span>-</span>
          <input type="text" name="phone2" placeholder="0000" maxlength="4" required>
          <span>-</span>
          <input type="text" name="phone3" placeholder="0000" maxlength="4" required>
        </div>
      </div>
      
      <!-- 성별 -->
      <div class="form-group">
        <label>성별</label>
        <div style="display: flex; gap: 20px;">
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="radio" name="gender" value="M" checked> 남자
          </label>
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="radio" name="gender" value="F"> 여자
          </label>
        </div>
      </div>
      
      <!-- 취미 -->
      <div class="form-group">
        <label>취미</label>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="checkbox" name="hobby" value="독서"> 독서
          </label>
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="checkbox" name="hobby" value="영화"> 영화감상
          </label>
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="checkbox" name="hobby" value="게임"> 게임
          </label>
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="checkbox" name="hobby" value="스포츠"> 스포츠
          </label>
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="checkbox" name="hobby" value="음악"> 음악감상
          </label>
          <label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
            <input type="checkbox" name="hobby" value="여행"> 여행
          </label>
        </div>
      </div>
      
      <!-- 버튼 -->
      <div class="btn-group">
        <button type="button" class="cancel" onclick="location.href='main.do';">취소</button>
        <button type="submit">가입하기</button>
      </div>
    </form>
  </div>
  
  <script>
    function validateForm() {
      const id = document.getElementById('id').value;
      const pw = document.getElementById('pw').value;
      const pw_confirm = document.getElementById('pw_confirm').value;
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      
      // 아이디 검증
      if (id.length < 4 || id.length > 16) {
        alert('아이디는 4자 이상 16자 이하여야 합니다.');
        return false;
      }
      
      // 비밀번호 검증
      if (pw.length < 8 || pw.length > 16) {
        alert('비밀번호는 8자 이상 16자 이하여야 합니다.');
        return false;
      }
      
      // 비밀번호 일치 확인
      if (pw !== pw_confirm) {
        alert('비밀번호가 일치하지 않습니다.');
        return false;
      }
      
      // 이름 검증
      if (name.trim() === '') {
        alert('이름을 입력해주세요.');
        return false;
      }
      
      // 이메일 검증
      if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
        alert('올바른 이메일 형식을 입력해주세요.');
        return false;
      }
      
      alert('회원가입이 완료되었습니다!');
      return true;
    }
    
    function checkId() {
      const id = document.getElementById('id').value;
      if (id === '') {
        alert('아이디를 입력해주세요.');
        return;
      }
      if (id.length < 4 || id.length > 16) {
        alert('아이디는 4자 이상 16자 이하여야 합니다.');
        return;
      }
      alert('사용 가능한 아이디입니다!');
    }
    
    function sendEmailCode() {
      const email = document.getElementById('email').value;
      if (email === '') {
        alert('이메일을 입력해주세요.');
        return;
      }
      alert('인증번호가 ' + email + '로 전송되었습니다.');
    }
    
    function verifyEmailCode() {
      const code = document.getElementById('email_code').value;
      if (code === '') {
        alert('인증번호를 입력해주세요.');
        return;
      }
      alert('이메일 인증이 완료되었습니다!');
    }
  </script>
</body>
</html>
