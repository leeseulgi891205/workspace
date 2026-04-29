package com.java.www.service;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.java.www.dao.MemberDao;
import com.java.www.dto.MemberDto;

public class MLoginServiceImpl implements MemberService {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		//섹션연결
		HttpSession session = request.getSession();
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		System.out.println(id+","+pw);
		//dao호출 id,pw가 있는지 확인
		MemberDao mdao = new MemberDao();
		MemberDto mdto = mdao.memberLogin(id,pw);
		if(mdto != null) {
			session.setAttribute("session_id", mdto.getId());
			session.setAttribute("session_name", mdto.getName());
		}
		request.setAttribute("mdto", mdto);
		
	}

}
