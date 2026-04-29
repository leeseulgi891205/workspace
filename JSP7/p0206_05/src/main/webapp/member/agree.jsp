<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>회원 가입 - 약관동의</title>
  <style>
    /* Pretendard 폰트 불러오기 */
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
        font-weight: 400;
        font-display: swap;
    }
    @font-face {
        font-family: 'Pretendard';
        src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Bold.woff') format('woff');
        font-weight: 700;
        font-display: swap;
    }
    * { font-family: 'Pretendard'; }
    ul, ol { list-style: none; padding: 0; margin: 0; }

    body {
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

    .container {
      width: 100%;
      max-width: 720px;
      margin: 0 auto;
      box-sizing: border-box;
    }

    .title {
        margin: 0 auto;
        text-align: center;
        padding: 70px 0;
        font-size: 30px;
        font-weight: bold;
    }

    .orderStep {
        text-align: center;
        padding-bottom: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #1a1a1a;
    }

    .orderStep ul {
        display: flex;
        justify-content: center;
        gap: 40px;
    }

    .orderStep li {
      display: inline-block;
      font-size: 14px;
    }

    .orderStep li .current {
        color: #035fe0;
        font-weight: 700;
        font-size: 15px;
    }

    .agreement-box {
        max-width: 600px;
        margin: 30px auto;
        padding: 20px;
        box-sizing: border-box;
    }

    .all-agree {
        padding: 15px;
        border: 2px solid #035fe0;
        margin-bottom: 20px;
        font-weight: bold;
    }

    .agreement-item {
        border: 1px solid #ccc;
        margin-bottom: 15px;
        padding: 15px;
    }

    .agreement-item h3 {
        margin: 0 0 10px 0;
        font-size: 15px;
    }

    .agreement-item h3 span {
        color: #035fe0;
    }

    .agreement-content {
        background: #f9f9f9;
        padding: 10px;
        font-size: 13px;
        color: #636363;
        max-height: 100px;
        overflow-y: auto;
    }

    .btn-box {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 30px;
    }

    .btn {
        width: 160px;
        height: 45px;
        border: none;
        font-size: 15px;
        cursor: pointer;
        border-radius: 4px;
    }

    .btn.cancel {
        background: #6c757d;
        color: white;
    }

    .btn.submit {
        background: #035fe0;
        color: white;
    }

    .btn:hover {
        opacity: 0.9;
    }
  </style>
</head>
<body>
  <div class="header">
    <div class="top-menu">
      <a href="agree.do">회원가입</a> |
      <a href="login.do">로그인</a> |
      <a href="#">주문조회</a> |
      <a href="index.do">홈으로</a>
    </div>
  </div>
  <div class="container">
    <div class="steps">
      <div class="title">회원가입</div>
      <div class="orderStep">
        <ul>
          <li><span class="current">1. 약관동의</span></li>
          <li>2. 정보입력</li>
          <li>3. 가입완료</li>
        </ul>
      </div>
    </div>
    <div class="agreement-box">
      <form id="agreeForm" action="membership.do" method="get">
        <div class="all-agree">
          <label><input type="checkbox" id="all-agree-checkbox"> 전체 동의</label>
        </div>
        <div class="agreement-item">
          <h3>
            <label><input type="checkbox" class="agree-checkbox required-checkbox"> 이용약관 동의 <span>(필수)</span></label>
          </h3>
          <div class="agreement-content">
            [이용약관] 제1조 (목적) 본 약관은 [회사명] (이하 "회사")가 제공하는 모든 서비스의 이용과 관련하여 회원의 권리, 의무 및 책임사항, 기타 필요한 사항을 규정함을 목적으로 합니다.
            제2조 (용어의 정의) 본 약관에서 사용하는 용어의 정의는 다음과 같습니다. 1. "서비스"라 함은 구현되는 단말기와 상관없이 회원이 이용할 수 있는 회사의 제반 서비스를 의미합니다.
          </div>
        </div>
        <div class="agreement-item">
          <h3>
            <label><input type="checkbox" class="agree-checkbox required-checkbox"> 개인정보 수집 및 이용 동의 <span>(필수)</span></label>
          </h3>
          <div class="agreement-content">
            [개인정보 수집 및 이용 동의] 수집항목: 이름, 아이디, 비밀번호, 휴대전화, 이메일 주소.
            수집목적: 회원관리 및 서비스 제공, 맞춤형 서비스 제공.
          </div>
        </div>
        <div class="agreement-item">
          <h3>
            <label><input type="checkbox" class="agree-checkbox"> 개인정보 제3자 제공 동의 <span>(선택)</span></label>
          </h3>
          <div class="agreement-content">
            [개인정보 제3자 제공] 제공대상: 제휴사, 파트너사. 제공목적: 이벤트, 프로모션, 마케팅.
          </div>
        </div>
        <div class="agreement-item">
          <h3>
            <label><input type="checkbox" class="agree-checkbox"> 쇼핑정보 수신 동의 <span>(선택)</span></label>
          </h3>
          <div class="agreement-content">
            할인쿠폰 및 이벤트, 맞춤 상품 추천 등 쇼핑정보를 SMS, 이메일로 받아볼 수 있습니다.
          </div>
        </div>
        <div class="btn-box">
          <button type="button" class="btn cancel" onclick="location.href='index.do'">취소</button>
          <button type="submit" class="btn submit">다음</button>
        </div>
      </form>
    </div>
  </div>
  <script>
    const allAgreeCheckbox = document.getElementById('all-agree-checkbox');
    const agreeCheckboxes = document.querySelectorAll('.agree-checkbox');
    const agreeForm = document.getElementById('agreeForm');
    const requiredCheckboxes = document.querySelectorAll('.required-checkbox');

    allAgreeCheckbox.addEventListener('change', (event) => {
      const isChecked = event.target.checked;
      agreeCheckboxes.forEach((checkbox) => {
        checkbox.checked = isChecked;
      });
    });

    agreeForm.addEventListener('submit', (e) => {
      let allRequiredChecked = true;
      requiredCheckboxes.forEach((checkbox) => {
        if (!checkbox.checked) {
          allRequiredChecked = false;
        }
      });

      if (!allRequiredChecked) {
        e.preventDefault();
        alert('필수 약관에 모두 동의해주세요.');
      }
    });
  </script>
</body>
</html>
