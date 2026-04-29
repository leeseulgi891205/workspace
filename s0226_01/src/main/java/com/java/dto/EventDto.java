package com.java.dto;

import java.sql.Timestamp;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@AllArgsConstructor
@NoArgsConstructor
@Data
public class EventDto {

	private Integer eno; // 이벤트 일련번호
	private String etitle; // 제목
	private String econtent; // 내용
	private Timestamp startdate; // 이벤트 시작일
	private Timestamp enddate; // 이벤트 종료일
	private String imageUrl; // 배너 이미지 경로 (배너)
	private String imageUrl2; // 배너 이미지 경로 (이미지)
	private Timestamp crdate; // 등록일
	private Timestamp update; // 수정일
	private int ehit; // 조회수
	private Timestamp status; // 진행상태
}
