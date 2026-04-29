package com.java.www.service;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.java.www.dto.MemberDto;

public class MemberList {
	public void execute(HttpServletRequest request, HttpServletRequest response) {
		MemberDto m = new MemberDto("aaa","1111","홍길동","010-1234-5678",
				"aaa@naver.com","남자","게임");
		request.setAttribute("member", m);
		
	}
}
