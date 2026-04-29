package com.java.www.service;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.dto.MemberDto;

public class MemberList2 {
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		List<MemberDto> list = new ArrayList<>();
		for (int i = 1; i <= 100; i++) {
			String idx = String.format("%03d", i);
			list.add(new MemberDto("user" + idx, "pw" + idx, "홍길동" + idx,
					"010-1234-" + idx, "user" + idx + "@naver.com", "남자", "게임"));
		}

		request.setAttribute("memberList", list);
	}
}