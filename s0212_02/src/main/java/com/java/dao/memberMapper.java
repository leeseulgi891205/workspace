package com.java.dao;

import org.apache.ibatis.annotations.Mapper;

import com.java.dto.MemberDto;

@Mapper
// @Component ,@Controller, @Service, @Repository, @Configuration, @Bean
public interface memberMapper {

	// 로그인 확인
	MemberDto selectLogin(MemberDto mdto);

	// 회원가입 확인
	int insertMember(MemberDto mdto);

}
