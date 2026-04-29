package com.java.www.service;

import java.io.UnsupportedEncodingException;
import java.util.Arrays;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.dao.MemberDao;

public class MInsertServiceImpl implements MemberService {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		try {request.setCharacterEncoding("utf-8");
		} catch (Exception e) {e.printStackTrace();}
		
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		String name = request.getParameter("name");
		String phone1 = request.getParameter("phone1");
		String phone2 = request.getParameter("phone2");
		String phone3 = request.getParameter("phone3");
		String phone = phone1+"-"+phone2+"-"+phone3;
		String email = request.getParameter("email");
		String gender = request.getParameter("gender");
		String[] hobbys = request.getParameterValues("hobby");
		String hobby = Arrays.toString(hobbys);
		
		MemberDao mdao = new MemberDao();
		mdao.memberInsert(id,pw,name,phone,email,gender,hobby);

	}

}
