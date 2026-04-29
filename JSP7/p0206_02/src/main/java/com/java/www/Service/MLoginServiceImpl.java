package com.java.www.Service;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import com.java.www.Dao.MemberDao;
import com.java.www.Dto.MemberDto;

public class MLoginServiceImpl implements MemberService {

    @Override
    public void execute(HttpServletRequest request, HttpServletResponse response) {
        String id = request.getParameter("id");
        String pw = request.getParameter("pw");
        
        MemberDao memberDao = new MemberDao();
        MemberDto memberDto = memberDao.memberLogin(id, pw);
        
        if (memberDto != null) {
            // 로그인 성공 - 세션에 회원정보 저장
            HttpSession session = request.getSession();
            session.setAttribute("sessionId", memberDto.getId());
            session.setAttribute("sessionName", memberDto.getName());
            request.setAttribute("mdto", memberDto);
        } else {
            // 로그인 실패
            request.setAttribute("mdto", null);
        }
    }
}
