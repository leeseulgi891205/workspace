package com.java.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

public class MemberController {

	@Autowired
	MemberService memberService;

	@GetMapping("/member/login")
	public String login(@RequestParam String id, Model model) {
		System.out.println("id,pw : " + id);
		return "login";
	}
}
