<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ page import="java.io.File" %>
<%@ page import="java.sql.Connection, java.sql.PreparedStatement" %>
<%@ page import="javax.naming.Context, javax.naming.InitialContext" %>
<%@ page import="javax.sql.DataSource" %>

<%@ page import="com.oreilly.servlet.MultipartRequest" %>
<%@ page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy" %>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>writeOk</title>
</head>
<body>
<h2>글 등록 완료</h2>

<%
    // 1) 업로드 경로 세팅
    String uploadPath = application.getRealPath("/upload");
    File dir = new File(uploadPath);
    if(!dir.exists()) dir.mkdirs();

    // 2) 업로드 제한 용량 (10MB)
    int size = 10 * 1024 * 1024;

    Connection conn = null;
    PreparedStatement pstmt = null;

    try {
        // 3) multipart 처리 (여기서 파일 저장됨)
        MultipartRequest multi = new MultipartRequest(
            request,
            uploadPath,
            size,
            "UTF-8",
            new DefaultFileRenamePolicy()
        );

        // 4) 폼 데이터 받기
        String writer = multi.getParameter("writer");  // 작성자
        String title  = multi.getParameter("title");   // 제목
        String content = multi.getParameter("content");// 내용

        // 5) 파일 받기 (input type="file" name="bfile" 기준)
        String fileField = "bfile";
        String fileName = multi.getFilesystemName(fileField); // 서버에 저장된 파일명(중복시 바뀐 이름)
        String oriName  = multi.getOriginalFileName(fileField); // 원본 파일명

        // 6) DB insert (커넥션풀)
        Context init = new InitialContext();
        DataSource ds = (DataSource)init.lookup("java:comp/env/jdbc/Oracle21");
        conn = ds.getConnection();

       
