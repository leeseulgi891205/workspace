package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class EventController {

	@GetMapping("/event/list")
	public String eventList() {
		return "event_list";
	}

	@GetMapping("/event/write")
	public String eventWrite() {
		return "write";
	}
}
