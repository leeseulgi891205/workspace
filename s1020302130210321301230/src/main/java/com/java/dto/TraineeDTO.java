package com.java.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TraineeDTO {
	private String name;      // 연습생 이름
	private String genre;     // 장르 (청량, 힙합, 발라드, 댄스)
	private int vocal;        // 보컬 점수
	private int dance;        // 댄스 점수
	private String image;     // 이미지 파일명
}
