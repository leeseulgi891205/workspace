<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>파일업로드</title>
	</head>
	<body>
		<h2>파일업로드완료</h2>
		<%
			String contentType = request.getContentType();
			
			// Check if the request is multipart/form-data
			if(contentType == null || !contentType.startsWith("multipart/form-data")) {
				out.println("<p style='color:red;'><strong>오류: 파일 업로드 폼에서만 접근할 수 있습니다.</strong></p>");
				out.println("<p>요청 Content-Type: " + contentType + "</p>");
				out.println("<p><a href='write_view.html'>돌아가기</a></p>");
			} else {
				String uploadPath = application.getRealPath("/upload");
				
				// Create upload directory if it doesn't exist
				java.io.File uploadDir = new java.io.File(uploadPath);
				if(!uploadDir.exists()) {
					uploadDir.mkdirs();
				}
				
				// Debug: 업로드 경로 표시
				out.println("<!-- 업로드 경로: "+uploadPath+" --><br>");
				
				int size = 10*1024*1024; //10MB : 1kb = 1024byte -> 1MB = 1024kb
				// MultipartRequest(request, 저장경로, 최대용량, 인코딩타입, 파일이름중복처리객체)
				MultipartRequest multi = new MultipartRequest(request, uploadPath, size, "utf-8", new DefaultFileRenamePolicy());

				String id = multi.getParameter("id");
				String btitle = multi.getParameter("btitle");
				String bcontent = multi.getParameter("bcontent");
				String bfile = multi.getFilesystemName("bfile"); //실제 업로드된 파일명
				
				out.println("<h3>업로드 완료</h3>");
				out.println("작성자 : "+id+"<br>");
				out.println("제목 : "+btitle+"<br>");
				out.println("내용 : "+bcontent+"<br>");
				
				// 파일 정보 표시
				if(bfile != null && !bfile.isEmpty()) {
					// 파일이 실제로 저장되었는지 확인
					java.io.File uploadedFile = new java.io.File(uploadPath, bfile);
					if(uploadedFile.exists()) {
						out.println("파일명 : "+bfile+"<br>");
						out.println("파일크기 : "+(uploadedFile.length()/1024)+" KB<br>");
						out.println("<p><a href='upload/"+bfile+"' target='_blank'>업로드된 파일 보기</a></p>");
					} else {
						out.println("<p style='color:red;'>파일이 저장되지 않았습니다.</p>");
						out.println("파일명: "+bfile+"<br>");
						out.println("경로: "+uploadPath+"<br>");
					}
				} else {
					out.println("업로드된 파일이 없습니다.<br>");
				}
				
				out.println("<br><a href='write_view.html'>목록으로 돌아가기</a>");
			}
		%>
	
	</body>
</html>