package com.java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.java.Service.MemberService;
import com.java.dto.MemberDto;

import jakarta.servlet.http.HttpSession;

@Controller
@RequestMapping("/member")
public class MemberController {
	@Autowired
	HttpSession session;

	@Autowired
	MemberService memberService;

	@GetMapping("/mlist")
	public String mlist(Model model) {
		List<MemberDto> list = memberService.selectAll();
		model.addAttribute("list", list);
		return "member/mlist";
	}

}
