package com.java.www.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.java.www.service.MInsertServiceImpl;
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
	    
	    switch(fileName) {	// 요청된 파일 이름에 따른 처리
	    case "/index.do":	
	    	viewPage = "./index.jsp";
	    	break;
	    case "/login.do":
	    	viewPage = "./member/login.jsp";
	    	break;
	    case "/doLogin.do":	// 로그인 처리
	    	memberService = new MLoginServiceImpl();	// 로그인 서비스 객체 생성
	    	memberService.execute(request, response);	// 로그인 서비스 실행
	    	viewPage = "./member/doLogin.jsp";	// 로그인 처리 후 뷰 페이지 설정
	    	break;
    case "/logout.do":	// 로그아웃 처리
    	HttpSession session = request.getSession();	// 세션 객체 가져오기
    	session.invalidate();	// 세션 무효화
    	request.setAttribute("logout", 1);	// 로그아웃 상태 설정
    	viewPage = "./member/doLogout.jsp";	// 로그아웃 처리 후 뷰 페이지 설정
    	break;
    case "/agree.do":	// 약관동의 페이지
    	viewPage = "./member/agree.jsp";	// 약관동의 페이지
    	break;
    case "/membership.do":	// 회원가입 페이지
    	viewPage = "./member/membership.jsp";	// 회원가입 폼 페이지
    	break;
    case "/doMembership.do":	// 회원가입 처리
    	memberService = new MInsertServiceImpl();	// 회원가입 서비스 객체 생성
    	memberService.execute(request, response);	// 회원가입 서비스 실행
    	viewPage = "./member/doMembership.jsp";	// 회원가입 처리 후 뷰 페이지 설정
    	break;
    case "/membershipComplete.do":	// 회원가입 완료 페이지
    	viewPage = "./member/membershipComplete.jsp";	// 회원가입 완료 페이지
    	break;
	    }//switch
	    
	    RequestDispatcher dispatcher = request.getRequestDispatcher(viewPage);	// 뷰 페이지로 포워딩
	    dispatcher.forward(request, response);	// 요청과 응답 객체 전달
	    
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {	// GET 요청 처리
		doAction(request, response);	// 공통 처리 메서드 호출
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {	// POST 요청 처리
		doAction(request, response);	// 공통 처리 메서드 호출
	}

}
