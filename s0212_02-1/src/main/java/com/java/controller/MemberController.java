package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import jakarta.servlet.http.HttpSession;

@Controller
@RequestMapping("/member")
public class MemberController {

	// 1. 로그인 폼 화면으로 이동
	@GetMapping("/login")
	public String loginForm() {
		return "member/login";
	}

	// 2. 실제 로그인 처리 (세션 저장)
	@PostMapping("/login")
	public String loginProcess(String id, String password, HttpSession session, Model model) {
		// 원래는 DB에서 select 해와서 비교해야 합니다. (추후 MyBatis로 교체할 부분)
		// 임시 테스트용 조건문: 아이디가 admin이고 비밀번호가 1234면 로그인 성공
		if ("admin".equals(id) && "1234".equals(password)) {
			// 로그인 성공 시 세션에 아이디와 이름 저장
			session.setAttribute("sessionId", id);
			session.setAttribute("sessionName", "메인 프로듀서"); // DB에서 가져온 이름

			return "redirect:/main"; // 로그인 성공 시 메인 화면으로 이동
		} else {
			// 로그인 실패 시 에러 메시지를 담아서 다시 로그인 화면으로
			model.addAttribute("loginError", "아이디 또는 비밀번호가 일치하지 않습니다.");
			return "member/login";
		}
	}

	// 3. 로그아웃 처리
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate(); // 세션 정보 모두 삭제
		return "redirect:/main"; // 로그아웃 후 메인 화면으로 이동
	}
}
