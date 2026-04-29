package com.java.www.controller;

import java.io.IOException;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.java.www.dto.BoardDto;
import com.java.www.dto.MemberDto;
import com.java.www.service.BListServiceImpl;
import com.java.www.service.BoardService;
import com.java.www.service.MInsertServiceImpl;
import com.java.www.service.MListServiceImpl;
import com.java.www.service.MLoginServiceImpl;
import com.java.www.service.MemberService;


@WebServlet("*.do")
public class FController extends HttpServlet {
	
	protected void doAction(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	    System.out.println("doAction");
	    String uri = request.getRequestURI();
	    String contextPath = request.getContextPath();
	    String fileName = uri.substring(contextPath.length());
	    String viewPage = "";
	    MemberService memberService = null;
	    BoardService boardService = null;
	    
	    switch(fileName) {
	    case "/index.do":
	    	viewPage = "./index.jsp";
	    	break;
	    case "/login.do":
	    	viewPage = "./member/login.jsp";
	    	break;
	    case "/doLogin.do":
	    	//다른클래스를 호출하려면 객체선언이 되어야 함.
	    	memberService = new MLoginServiceImpl();
	    	memberService.execute(request, response);
	    	viewPage = "./member/doLogin.jsp";
	    	break;
	    case "/logout.do":
	    	HttpSession session = request.getSession();
	    	session.invalidate();
	    	request.setAttribute("logout", 1);
	    	viewPage = "./member/doLogout.jsp";
	    	break;
	    case "/member.do": //전체회원리스트
	    	memberService = new MListServiceImpl();
	    	memberService.execute(request, response);
	    	viewPage = "./member/member.jsp";
	    	break;	
	    case "/membership.do":   //회원가입페이지
	    	viewPage = "./member/membership.jsp";
	    	break;
	    case "/doMembership.do": //회원가입저장
	    	memberService = new MInsertServiceImpl();
	    	memberService.execute(request, response);
	    	viewPage = "./member/membership2.jsp";
	    	break;
	    case "/board.do": //전체게시글리스트
	    	boardService = new BListServiceImpl();
	    	boardService.execute(request, response);
	    	viewPage = "./board/board.jsp";
	    	break;
	    	
	    }//switch
	    
	    RequestDispatcher dispatcher = request.getRequestDispatcher(viewPage);
	    dispatcher.forward(request, response);
	    
	}//
	
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doAction(request,response);
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doAction(request,response);
	}

}
