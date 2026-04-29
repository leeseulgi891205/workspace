package com.java.www.service;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.java.www.dto.MemberDto;

public class MemberList2 {
	public void execute(HttpServletRequest request, HttpServletRequest response) {
		List<MemberDto> list = new ArrayList()<MemberDto>();
		list.add(new MemberDto("aaa","1111","홍길동","010-1234-5678",
				"aaa@naver.com","남자","게임"));
		list.add(new MemberDto("bbb","2222","홍길순","010-1234-5678",
				"bbb@naver.com","여자","게임"));
		
		request.setAttribute("member", m);
		
	}
}
