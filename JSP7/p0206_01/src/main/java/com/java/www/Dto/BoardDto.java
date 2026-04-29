package com.java.www.Dto;

public class BoardDto {
	
	public BoardDto() {}
	public BoardDto(int bno, String title, String content, String writer, String indate) {
		this.bno = bno;
		this.title = title;
		this.content = content;
		this.writer = writer;
		this.indate = indate;
	}
	
	private int bno;
	private String title;
	private String content;
	private String writer;
	private String indate;
	
	public int getBno() {
		return bno;
	}
	public void setBno(int bno) {
		this.bno = bno;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public String getIndate() {
		return indate;
	}
	public void setIndate(String indate) {
		this.indate = indate;
	}
	
}
