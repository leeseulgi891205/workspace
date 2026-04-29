package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BoardController {
	
	@GetMapping("/board/blist")
	public String blist() {
		return "blist";
	}
	
	@GetMapping("/board/bwrite")
	public String bwrite() {
		return "bwrite";
	}

}
