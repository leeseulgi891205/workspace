package com.java.www.service;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.dao.MemberDao;
import com.java.www.dto.MemberDto;

public class MemberList {

    public void execute(HttpServletRequest request, HttpServletResponse response) {
        MemberDao memberDao = new MemberDao();
        List<MemberDto> list = memberDao.memberList();
        System.out.println("MemberList service list.size() : " + list.size());

        request.setAttribute("memberList", list);
    }
}
