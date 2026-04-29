package com.java.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.sql.Timestamp;

@Builder
@NoArgsConstructor
@AllArgsConstructor
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
	private Timestamp brdate;
	private Timestamp bdate;
}