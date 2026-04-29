package com.java.www.service;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.java.www.dao.MemberDao;
import com.java.www.dto.MemberDto;

public class MLoginServiceImpl implements MemberService {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) {// 서비스 실행 메서드
		try {// 한글 인코딩 처리
			request.setCharacterEncoding("utf-8");
		} catch (Exception e) {// 인코딩 예외 처리
			e.printStackTrace();// 예외 발생 시 스택 트레이스 출력
		}
		
		String id = request.getParameter("id");	// 사용자로부터 입력받은 아이디
		String pw = request.getParameter("pw");	// 사용자로부터 입력받은 비밀번호
		
		MemberDao mdao = new MemberDao();	// MemberDao 객체 생성
		MemberDto mdto = mdao.selectOne(id, pw);	// 아이디와 비밀번호로 회원 정보 조회
		
		if(mdto != null) {	
			// 로그인 성공 - 세션에 사용자 정보 저장
			HttpSession session = request.getSession();	// 세션 객체 가져오기
			session.setAttribute("session_id", mdto.getId());	// 세션에 아이디 저장
			session.setAttribute("session_name", mdto.getName());	// 세션에 이름 저장
			System.out.println("[DEBUG] Login session created for id: " + mdto.getId());	// 디버그 메시지 출력
			request.setAttribute("login", 1);	// 로그인 성공 상태 설정
		} else {
			// 로그인 실패
			System.out.println("[DEBUG] Login failed - wrong credentials");	// 디버그 메시지 출력
			request.setAttribute("login", 0);	// 로그인 실패 상태 설정
		}
	}

}
