package com.java.dto;

import java.sql.Timestamp;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@AllArgsConstructor
@NoArgsConstructor
@Data
@Entity // 자동으로 테이블이 생성됨
public class MemberDto {

	@Id
	@Column(length = 50)
	private String id;
	@Column(length = 100, nullable = false)
	private String pw;
	@Column(length = 50, nullable = false)
	private String name;
	@Column(length = 13)
	private String phone;
	@Column(length = 50)
	private String email;
	@Column(length = 6)
	@ColumnDefault(" '남자' ")
	private String gender;
	@Column(length = 50)
	private String hobby;
	@CreationTimestamp // 자동으로 현재 날짜가 입력됨
	private Timestamp mdate;
}
