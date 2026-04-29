package com.java.Dto;

import lombok.Data;

@Data
public class MemberDto {

	private String id;
	private String pw;
	private String name;
	private String email;
	private String phone;
	private String gender;
	private String[] hobby;
}
