package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class FController {

	// 메인 페이지 (index)
	@GetMapping("/")
	public String index() {
		return "index";
	}
	
	// main 페이지
	@GetMapping("/main")
	public String main() {
		return "main";
	}
	
	// 로그인 페이지
	@GetMapping("/login")
	public String login() {
		return "login";
	}
	
	// 관리자 로그인 페이지
	@GetMapping("/admin/login")
	public String adminLogin() {
		return "admin_login";
	}
	
	// 관리자 계정 페이지
	@GetMapping("/admin/account")
	public String adminAccount() {
		return "admin_account";
	}
	
	// 회원가입 - 약관동의
	@GetMapping("/join/terms")
	public String joinTerms() {
		return "join01_terms";
	}
	
	// 회원가입 - 정보입력
	@GetMapping("/join/info")
	public String joinInfo() {
		return "join02_info_input";
	}
	
	// 회원가입 - 완료
	@GetMapping("/join/success")
	public String joinSuccess() {
		return "join03_success";
	}
	
	// 이벤트 목록
	@GetMapping("/event/list")
	public String eventList() {
		return "event_list";
	}
	
	// 이벤트 상세
	@GetMapping("/event/read")
	public String eventRead() {
		return "event_read";
	}
	
	// 공지사항 목록
	@GetMapping("/notice/list")
	public String noticeList() {
		return "notice_list";
	}
	
	// 공지사항 상세
	@GetMapping("/notice/read")
	public String noticeRead() {
		return "notice_read";
	}
	
	// 글쓰기
	@GetMapping("/write")
	public String write() {
		return "write";
	}
	
	// 회원정보 수정
	@GetMapping("/member/modify")
	public String modifyMemberInfo() {
		return "modifying_member_info";
	}
	
}
