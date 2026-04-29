package com.java.www.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
// NOTE: We map this servlet in web.xml to avoid annotation-scan issues on some Tomcat/Eclipse setups.
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.service.MemberList;
import com.java.www.service.MemberList2;

public class FController extends HttpServlet {
	protected void doAction(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doAction");
		//fileName 검색
		request.setCharacterEncoding("utf-8");
		String viewPage = null;
		String uri = request.getRequestURI();          // /p0205_03/main.do
		System.out.println("uri : "+uri);
		String contextPath = request.getContextPath(); // /p0205_03
		System.out.println("contextPath : "+contextPath);
		String fileName = uri.substring(contextPath.length()); // /main.do
		System.out.println("fileName : "+fileName);
		
		switch(fileName) {
		case "/main.do":
			MemberList2 mList = new MemberList2();
			mList.execute(request, response);
			viewPage = "./main.jsp";
			break;
		case "/member.do":
			viewPage = "./member.jsp";
			break;
		case "/membership.do":
			viewPage = "./membership.jsp";
			break;
		case "/board.do":
			viewPage = "./board.jsp";
			break;
		case "/bwrite.do":
			viewPage = "./bwrite.jsp";
			break;
		default:
			viewPage = "./main.jsp";
			break;
		}
		
		
		if (viewPage == null) {
			viewPage = "./main.jsp";
		}
		System.out.println("viewPage : "+viewPage);
		// request의 데이터가 함께 포워드
		RequestDispatcher dispatcher = request.getRequestDispatcher(viewPage);
		if(dispatcher != null) {
			dispatcher.forward(request, response);
		} else {
			System.out.println("ERROR: dispatcher is null for viewPage: " + viewPage);
			response.sendError(HttpServletResponse.SC_NOT_FOUND, "Page not found: " + viewPage);
		}
	}
	
	
	
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doAction(request,response);
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doAction(request,response);
	}

}