package com.java.www.service;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.Dao.MemberDao;
import com.java.www.Dto.MemberDto;

public class MemberServiceImpl implements Memberservice {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		// searchId 속성이 있으면 검색 모드, 없으면 전체 조회 모드
		String searchId = (String) request.getAttribute("searchId");
		
		MemberDao mdao = new MemberDao();
		List<MemberDto> list = new ArrayList<>();
		
		if (searchId != null && !searchId.isEmpty()) {
			// 검색 모드
			list = mdao.searchById(searchId);
			System.out.println("MemberServiceImpl - search result size: " + list.size());
		} else {
			// 전체 조회 모드
			list = mdao.memberList();
			System.out.println("MemberServiceImpl - list size: " + list.size());
		}
		
		request.setAttribute("memberList", list);
		
	}

}
