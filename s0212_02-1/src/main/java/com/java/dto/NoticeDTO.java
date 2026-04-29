package com.java.dto;

import java.util.Date;

public class NoticeDTO {
	private int id;
	private String title;
	private String content;
	private Date created_at;

	// 기본 생성자
	public int getId() {
		return id;
	}

	// getter와 setter 메서드
	public void setId(int id) {
		this.id = id;
	}

	//
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

	public Date getCreated_at() {
		return created_at;
	}

	public void setCreated_at(Date created_at) {
		this.created_at = created_at;
	}
}
