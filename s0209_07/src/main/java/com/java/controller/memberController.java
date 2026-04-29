package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/member")
public class memberController {
	
	@GetMapping("/login")
	public String login() {
		return "member/login";
	}
	
	@PostMapping("/dologin")
	public String doLogin() {
		return "member/doLogin";
	}
	
	@GetMapping("/logout")
	public String logout() {
		return "member/logout";
	}
	
	@GetMapping("/join")
	public String join() {
		return "member/join";
	}


}
