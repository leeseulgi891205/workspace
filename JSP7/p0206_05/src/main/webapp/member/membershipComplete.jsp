<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원 가입 완료</title>
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
            background-color: #fafafa;
            color: #1a1a1a;
            line-height: 1.5;
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
            text-align: center;
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

        .message-box {
            max-width: 600px;
            margin: 50px auto;
            padding: 50px 20px;
            border-top: 1px solid #ccc;
            border-bottom: 1px solid #ccc;
            box-sizing: border-box;
        }

        .message-box p {
            font-size: 18px;
            font-weight: 500;
            color: #035fe0;
            margin-bottom: 30px;
        }

        .btn-box {
            display: flex;
            justify-content: center;
            gap: 15px;
        }

        .btn {
            width: 160px;
            height: 45px;
            border: none;
            font-size: 15px;
            cursor: pointer;
            border-radius: 4px;
        }

        .btn.home {
            background: #6c757d;
            color: white;
        }

        .btn.login {
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
        <div class="title">회원가입</div>
        <div class="orderStep">
            <ul>
                <li>1. 약관동의</li>
                <li>2. 정보입력</li>
                <li><span class="current">3. 가입완료</span></li>
            </ul>
        </div>
        <div class="message-box">
            <p>회원가입이 완료되었습니다!</p>
            <p style="font-size: 16px; color: #1a1a1a;">환영합니다. 지금 바로 로그인하여 다양한 서비스를 이용해보세요.</p>
        </div>
        <div class="btn-box">
            <button class="btn home" onclick="location.href='index.do'">홈으로</button>
            <button class="btn login" onclick="location.href='login.do'">로그인</button>
        </div>
    </div>
</body>
</html>
