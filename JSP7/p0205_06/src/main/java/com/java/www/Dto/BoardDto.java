package com.java.www.Dto;

public class BoardDto {
	private int no;				// 게시글 번호
	private String title;			// 게시글 제목
	private String writer;			// 작성자
	private String writeDate;		// 작성일
	private int views;				// 조회수
	private String content;			// 게시글 내용
	private String pwd;				// 비밀번호
	
	// 기본 생성자
	public BoardDto() {}
	
	// 게시글 목록용 생성자 (번호, 제목, 작성자, 작성일, 조회수)
	public BoardDto(int no, String title, String writer, String writeDate, int views) {
		this.no = no;
		this.title = title;
		this.writer = writer;
		this.writeDate = writeDate;
		this.views = views;
	}
	
	// 전체 정보 생성자
	public BoardDto(int no, String title, String writer, String writeDate, int views, String content, String pwd) {
		this.no = no;
		this.title = title;
		this.writer = writer;
		this.writeDate = writeDate;
		this.views = views;
		this.content = content;
		this.pwd = pwd;
	}
	
	// Getter, Setter
	public int getNo() {
		return no;
	}
	
	public void setNo(int no) {
		this.no = no;
	}
	
	public String getTitle() {
		return title;
	}
	
	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getWriter() {
		return writer;
	}
	
	public void setWriter(String writer) {
		this.writer = writer;
	}
	
	public String getWriteDate() {
		return writeDate;
	}
	
	public void setWriteDate(String writeDate) {
		this.writeDate = writeDate;
	}
	
	public int getViews() {
		return views;
	}
	
	public void setViews(int views) {
		this.views = views;
	}
	
	public String getContent() {
		return content;
	}
	
	public void setContent(String content) {
		this.content = content;
	}
	
	public String getPwd() {
		return pwd;
	}
	
	public void setPwd(String pwd) {
		this.pwd = pwd;
	}
}
