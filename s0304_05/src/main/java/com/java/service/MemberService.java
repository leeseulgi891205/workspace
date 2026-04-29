package com.java.service;

import java.util.List;

import com.java.dto.MemberDto;

public interface MemberService {
	
	MemberDto findById(String id);
	
	MemberDto findByIdAndPw(MemberDto mdto);
	
	List<MemberDto> findAll();
	
	void save(MemberDto mdto);
	
	void update(MemberDto mdto);
	
	void deleteById(MemberDto mdto);
}
