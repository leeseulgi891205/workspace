package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import jakarta.servlet.http.HttpSession;

@Controller
public class FController {

	@GetMapping({ "/", "/index" })
	public String index(String flag, HttpSession session, Model model) {
		model.addAttribute("flag", flag);
		session.invalidate();
		return "index";
	}
}
