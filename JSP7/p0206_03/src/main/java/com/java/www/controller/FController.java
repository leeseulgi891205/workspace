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
import com.java.www.service.BDeleteServiceImpl;
import com.java.www.service.BInsertServiceImpl;
import com.java.www.service.BListServiceImpl;
import com.java.www.service.BUpdateServiceImpl;
import com.java.www.service.BViewServiceImpl;
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
	    case "/index.do":	//처음화면
	    	viewPage = "./index.jsp";
	    	break;
	    case "/login.do":	//로그인페이지
	    	viewPage = "./member/login.jsp";
	    	break;
	    case "/doLogin.do":	//로그인처리
	    	//다른클래스를 호출하려면 객체선언이 되어야 함.
	    	memberService = new MLoginServiceImpl();
	    	memberService.execute(request, response);
	    	viewPage = "./member/doLogin.jsp";
	    	break;
	    case "/logout.do":	//로그아웃처리	
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
	    
	    case "/boardView.do": //게시글 상세보기
	    	boardService = new BViewServiceImpl();
	    	boardService.execute(request, response);
	    	viewPage = "./board/boardView.jsp";
	    	break;
	    	
	    case "/boardWrite.do": //게시글쓰기
	    	viewPage = "./board/boardwrite.jsp";
	    	break;
	    	
	    case "/doBoardWrite.do": //게시글쓰기저장 - insert
	    	boardService = new BInsertServiceImpl();
	    	boardService.execute(request, response);
	    	viewPage = "./board/doBoardWrite.jsp";
	    	break;
    	
    case "/doBoardDelete.do": //게시글 삭제 - delete
    	boardService = new BDeleteServiceImpl();
    	boardService.execute(request, response);
    	viewPage = "./board/doBoardDelete.jsp";
    	break;
    	
    case "/boardUpdate.do": //게시글 수정 페이지 호출 - select
    	boardService = new BViewServiceImpl();
    	boardService.execute(request, response);
    	viewPage = "./board/boardUpdate.jsp";
    	break;
    	
    case "/doBoardUpdate.do": //게시글 수정 실행 - update
    	boardService = new BUpdateServiceImpl();
    	boardService.execute(request, response);
    	viewPage = "./board/doBoardUpdate.jsp";
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