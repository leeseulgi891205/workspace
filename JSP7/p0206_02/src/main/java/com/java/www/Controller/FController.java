package com.java.www.Controller;

import java.io.IOException;
import java.util.List;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.Service.MemberService;
import com.java.www.Service.BoardService;
import com.java.www.Service.MLoginServiceImpl;
import com.java.www.Service.MemberRegistrationServiceImpl;
import com.java.www.Service.BoardServiceImpl;
import com.java.www.Dto.BoardDto;

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
        BoardService boardService = null;
        List<BoardDto> boardList = null;
        BoardDto boardDto = null;
        
        
        switch (fileName) {
            case "/main.do":
                viewPage = "/main.jsp";
                break;
                
            case "/login.do":
                viewPage = "/login.jsp";
                break;
            
            case "/dologin.do":
                memberService = new MLoginServiceImpl();
                memberService.execute(request, response);
                viewPage = "/dologin.jsp";
                break;
            
            case "/membership.do":
                viewPage = "/membership.jsp";
                break;
            
            case "/domembership.do":
                memberService = new MemberRegistrationServiceImpl();
                memberService.execute(request, response);
                viewPage = "/register_complete.jsp";
                break;
                
            case "/logout.do":
                request.getSession().invalidate();
                viewPage = "/main.jsp";
                break;
            
            case "/board.do":
                boardService = new BoardServiceImpl();
                boardService.execute(request, response);
                viewPage = "/board.jsp";
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
