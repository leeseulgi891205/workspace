package com.java.controller;

import org.springframework.web.bind.annotation.GetMapping;

public class FController {

	@GetMapping({ "/", "/index" })
	public String index() {
		return "index";
	}

}
