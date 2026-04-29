package com.java.www.service;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.Dao.MemberDao;
import com.java.www.Dto.MemberDto;

public class MemberListService {
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		MemberDao memberDao = new MemberDao();
		List<MemberDto> list = memberDao.selectAll();
		System.out.println("MemberListService list.size() : " + list.size());
		request.setAttribute("memberList", list);
	}
}

