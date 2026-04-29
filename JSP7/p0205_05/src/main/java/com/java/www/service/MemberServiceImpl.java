package com.java.www.service;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.Dao.MemberDao;
import com.java.www.Dto.MemberDto;

public class MemberServiceImpl implements Memberservice {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		MemberDao mdao = new MemberDao();
		List<MemberDto> list = mdao.memberList();
		System.out.println("MemberServiceImpl - list size: " + list.size());
		request.setAttribute("memberList", list);
	}

}
