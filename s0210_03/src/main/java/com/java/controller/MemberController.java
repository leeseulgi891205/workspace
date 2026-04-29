package com.java.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.servlet.http.HttpSession;

@Controller
public class MemberController {

	@Autowired // IOC컨테이너에서 시작할때 객체를 주입
	HttpSession session;

	@PostMapping("/member/logout")
	public String logout() {
		session.invalidate(); // 모든세션을 무효화
		return "redirect:/";
	}

	@GetMapping("/member/login")
	public String login(String flag, Model model) {
		System.out.println("flag : " + flag);
		model.addAttribute("flag", flag);
		return "login";
	}

	@PostMapping("/member/login")
	public String login(String id, String pw) {
		if ("aaa".equals(id) && "1111".equals(pw)) {
			return "redirect:/?flag=1";
		} else {
			return "redirect:/member/login?flag=2";
		}
	}

}