package com.java.www.Service;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.java.www.Dao.MemberDao;

public class MemberRegistrationServiceImpl implements MemberService {

    @Override
    public void execute(HttpServletRequest request, HttpServletResponse response) {
        String id = request.getParameter("id");
        String pw = request.getParameter("pw");
        String name = request.getParameter("name");
        String phone1 = request.getParameter("phone1");
        String phone2 = request.getParameter("phone2");
        String phone3 = request.getParameter("phone3");
        String email = request.getParameter("email");
        String gender = request.getParameter("gender");
        String[] hobbies = request.getParameterValues("hobby");
        
        String phone = phone1 + "-" + phone2 + "-" + phone3;
        String hobbyStr = "";
        
        if (hobbies != null) {
            hobbyStr = String.join(",", hobbies);
        }
        
        MemberDao memberDao = new MemberDao();
        boolean isSuccess = memberDao.memberInsert(id, pw, name, phone, email, gender, hobbyStr);
        
        if (isSuccess) {
            request.setAttribute("registerResult", "success");
        } else {
            request.setAttribute("registerResult", "fail");
        }
    }
}
