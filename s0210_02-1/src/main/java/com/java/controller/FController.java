package com.java.controller;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.java.Dto.MemberDto;

import jakarta.servlet.http.HttpServletRequest;

@Controller
public class FController {

	@GetMapping("/")
	public String index(HttpServletRequest request, Integer flag, Model model) {
		System.out.println("flag: " + flag);
		model.addAttribute("flag", flag);
		LocalDateTime now = LocalDateTime.now();
		model.addAttribute("now", now);
		// add formatted string to avoid JSTL fmt coercion issues
		model.addAttribute("nowFormatted", now.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
		Object m = request.getSession().getAttribute("member");
		if (m != null && m instanceof MemberDto) {
			model.addAttribute("member", (MemberDto) m);
		}
		return "index";
	}

}