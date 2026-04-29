package com.java.dto;

import java.sql.Timestamp;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder // 부분 생성자
@AllArgsConstructor // 전체 생성자
@NoArgsConstructor // 기본 생성자
@Data
public class BoardDto {

	private int bno;
	private String btitle;
	private String bcontent;
	private String id;
	private int bgroup;
	private int bstep;
	private int bindent;
	private int bhit;
	private String bfile;
	private Timestamp bdate;
}
