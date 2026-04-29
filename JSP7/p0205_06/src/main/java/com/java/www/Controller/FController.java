package com.java.www.Controller; // 패키지 선언(폴더/경로 역할)

import java.io.IOException; // 입출력 예외 처리에 필요
import javax.servlet.ServletException; // 서블릿 예외 처리에 필요
import javax.servlet.annotation.WebServlet; // 어노테이션으로 서블릿 매핑할 때 사용
import javax.servlet.http.HttpServlet; // 서블릿 클래스 상속
import javax.servlet.http.HttpServletRequest; // 요청 객체
import javax.servlet.http.HttpServletResponse; // 응답 객체
import javax.servlet.RequestDispatcher; // forward(포워딩)할 때 사용

import com.java.www.service.MemberServiceImpl; // 서비스 구현 클래스
import com.java.www.service.Memberservice; // 서비스 인터페이스(또는 공통 타입)
import com.java.www.service.BoardServiceImpl; // 게시판 서비스 구현 클래스
import com.java.www.service.BoardService; // 게시판 서비스 인터페이스

@WebServlet("*.do") // .do로 끝나는 모든 요청을 이 컨트롤러가 받음
public class FController extends HttpServlet {

    // doGet/doPost에서 공통으로 호출할 메서드
    protected void doAction(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        request.setCharacterEncoding("UTF-8"); // 요청 데이터 인코딩(POST 한글 처리)
        response.setContentType("text/html; charset=UTF-8"); // 응답 인코딩 설정

        System.out.println("doAction"); // 요청이 들어왔는지 확인용 로그

        String uri = request.getRequestURI(); // 요청 전체 URI (예: /프로젝트명/member.do)
        String contextPath = request.getContextPath(); // 프로젝트 경로 (예: /프로젝트명)
        String fileName = uri.substring(contextPath.length()); // 실제 매핑 경로만 추출 (예: /member.do)

        String viewPage = ""; // forward할 JSP 경로 저장
        Memberservice mService = null; // 서비스 객체를 담을 변수

        // 요청 경로(fileName)로 기능 분기
        switch (fileName) {

            case "/member.do":
                mService = new MemberServiceImpl(); // 회원목록/회원정보 관련 서비스 생성
                mService.execute(request, response); // 서비스 실행(데이터 조회 후 request에 저장)
                viewPage = "/member.jsp"; // 결과를 보여줄 JSP
                break;

            case "/main.do":
                viewPage = "/main.jsp"; // 메인 화면으로 이동
                break;

            case "/register.do":
                viewPage = "/register.jsp"; // 회원가입 화면으로 이동
                break;

            case "/search.do":
                viewPage = "/search.jsp"; // 회원검색 입력 화면으로 이동
                break;

            case "/searchOk.do":
                String searchId = request.getParameter("searchId"); // 검색할 아이디 파라미터 받기
                mService = new MemberServiceImpl(); // 검색 처리 서비스 생성
                request.setAttribute("searchId", searchId); // 서비스에서 쓰도록 request에 저장
                mService.execute(request, response); // 검색 실행(결과를 request에 저장)
                viewPage = "/searchResult.jsp"; // 검색 결과 화면으로 이동
                break;

            case "/login.do":
            case "/board.do":
                BoardService bService = new BoardServiceImpl(); // 게시판 서비스 생성
                bService.execute(request, response); // 게시판 목록 조회
                viewPage = "/board.jsp"; // 게시판 화면으로 이동
                break;

            case "/writeForm.do":
                viewPage = "/writeForm.jsp"; // 글쓰기 폼 화면으로 이동
                break;

            default:
                viewPage = "/main.jsp"; // 매칭되는 기능이 없으면 메인으로 이동
                break;
        }

        // viewPage가 비어있지 않으면 해당 JSP로 forward
        if (viewPage != null && !viewPage.isEmpty()) {
            RequestDispatcher dispatcher = request.getRequestDispatcher(viewPage); // 이동할 JSP 선택
            dispatcher.forward(request, response); // 서버 내부 이동(데이터 유지)
        }

    } // doAction

    // GET 요청 처리
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doAction(request, response); // 공통 처리 메서드 호출
    }

    // POST 요청 처리
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doAction(request, response); // 공통 처리 메서드 호출
    }

}
