package com.java.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class searchDto {

	private String searchWord;
	private String searchType;
	private int page;
	private int startRow;
	private int endRow;
}