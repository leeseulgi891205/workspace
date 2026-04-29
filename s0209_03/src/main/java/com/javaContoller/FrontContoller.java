package com.javaContoller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class FrontContoller {
	
	@Autowired
	Product product;
	
	@GetMapping({"/", "/index"}) // map both root and /index
	public String index() {
		System.out.println("test index");
		return "forward:/index.html";
	}
	
	@GetMapping("/member")
	public String member() {
		System.out.println("test member");
		return "forward:/member.html";
	}

}