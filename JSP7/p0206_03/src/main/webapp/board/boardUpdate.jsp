<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VLAST Shop - 게시글 수정</title>
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

    .write-container {
      max-width: 800px;
      margin: 80px auto;
      padding: 0 20px;
      box-sizing: border-box;
    }
    .write-title {
      font-size: 28px;
      font-weight: bold;
      margin-bottom: 30px;
      text-align: center;
    }

    form.write-form {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .write-form input[type="text"],
    .write-form textarea {
      padding: 10px;
      font-size: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      width: 100%;
    }

    .write-form textarea {
      resize: vertical;
      min-height: 200px;
    }

    .write-buttons {
      display: flex;
      justify-content: flex-end;
      gap: 15px;
    }

    .write-buttons button {
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      font-size: 14px;
      color: white;
      background-color: #035fe0;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    .write-buttons button:hover {
      background-color: #0046b3;
    }

    .write-buttons .cancel {
      background-color: #6c757d;
    }

    .write-buttons .cancel:hover {
      background-color: #5a6268;
    }

    footer {
      border-top: 1px solid #ccc;
      padding: 30px;
      text-align: center;
      font-size: 13px;
      color: #A0A0A0;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <div class="header">
    <div class="top-menu">
      <a href="#">회원가입</a> |
      <a href="#">로그인</a> |
      <a href="#">주문조회</a> |
      <a href="${pageContext.request.contextPath}/">홈으로</a>
    </div>
  </div>

  <!-- 수정 폼 -->
  <div class="write-container">
    <div class="write-title">게시글 수정</div>
    <form action="./doBoardUpdate.do" method="post" class="write-form" id="updateForm">
      <input type="hidden" name="bno" value="${board.bno}" />
      <input type="hidden" name="oldBFile" value="${board.bfile}" />
      <input type="text" name="id" id="id" placeholder="작성자" value="${board.id}" maxlength="20" readonly style="background-color: #f0f0f0;" />
      <input type="text" name="btitle" id="btitle" placeholder="제목" value="${board.btitle}" maxlength="100" required />
      <textarea name="bcontent" id="content" placeholder="내용을 입력하세요." maxlength="2000" required>${board.bcontent}</textarea>
      <input type="file" name="bfile" id="bfile" />
      <input type="hidden" name="bfile" value="${board.bfile}" />

      <div class="write-buttons">
        <button type="submit">수정</button>
        <button type="button" class="cancel" onclick="history.back()">취소</button>
      </div>
    </form>
  </div>

  <!-- Footer -->
  <footer>
    Copyright © VLAST Shop. All rights reserved.
  </footer>

  <script>
    const updateForm = document.getElementById('updateForm');

    updateForm.addEventListener('submit', (e) => {
      const title = document.getElementById('btitle').value.trim();
      const content = document.getElementById('content').value.trim();

      if (!title || !content) {
        e.preventDefault();
        alert('제목과 내용을 모두 입력해주세요.');
      }
    });
  </script>
</body>
</html>
