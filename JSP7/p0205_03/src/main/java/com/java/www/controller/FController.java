package com.java.www.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.service.MemberList2;

@WebServlet("*.do")
public class FController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private void doAction(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // ✅ POST 한글 처리 (GET은 server.xml URIEncoding 설정이 필요)
        request.setCharacterEncoding("UTF-8");

        String uri = request.getRequestURI();           // 예: /p0205_03/main.do
        String contextPath = request.getContextPath();  // 예: /p0205_03
        String fileName = uri.substring(contextPath.length()); // 예: /main.do

        System.out.println("doAction");
        System.out.println("uri : " + uri);
        System.out.println("contextPath : " + contextPath);
        System.out.println("fileName : " + fileName);

        String viewPage;

        switch (fileName) {
            case "/":
            case "/main.do": {
                MemberList2 mList = new MemberList2();
                mList.execute(request, response);
                viewPage = "/main.jsp";
                break;
            }

            case "/member.do":
                viewPage = "/member.jsp";
                break;

            case "/membership.do":
                viewPage = "/membership.jsp";
                break;

            case "/board.do":
                viewPage = "/board.jsp";
                break;

            case "/bwrite.do":
                viewPage = "/bwrite.jsp";
                break;

            default:
                response.sendRedirect(contextPath + "/main.do");
                return;
        }

        System.out.println("viewPage : " + viewPage);

        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPage);
        dispatcher.forward(request, response);
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doAction(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doAction(request, response);
    }
}
