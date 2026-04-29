package com.java.www.Controller;

import java.io.IOException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.Service.MemberService;
import com.java.www.Service.MLoginServiceImpl;
import com.java.www.Dto.MemberDto;

@WebServlet("*.do")
public class FController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doAction(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        
        String uri = request.getRequestURI();
        String contextPath = request.getContextPath();
        String fileName = uri.substring(contextPath.length());
        String viewPage = "";
        MemberService memberService = null;
        
        switch (fileName) {
            case "/main.do":
                viewPage = "/main.jsp";
                break;
                
            case "/login.do":
                viewPage = "/member/login.jsp";
                break;
            
            case "/dologin.do":
                memberService = new MLoginServiceImpl();
                memberService.execute(request, response);
                viewPage = "/member/dologin.jsp";
                break;
            
            case "/membership.do":
                viewPage = "/member/membership.jsp";
                break;
                
            case "/logout.do":
                viewPage = "/member/dologout.jsp";
                break;
            
            case "/member.do":
                viewPage = "/member/member.jsp";
                break;
                
            case "/board.do":
                viewPage = "/board/board.jsp";
                break;
                
            default:
                viewPage = "/main.jsp";
        }
        
        // 포워딩 처리
        if (viewPage != null && !viewPage.equals("")) {
            RequestDispatcher dispatcher = request.getRequestDispatcher(viewPage);
            dispatcher.forward(request, response);
        }
    }
    
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doAction(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doAction(request, response);
    }
}