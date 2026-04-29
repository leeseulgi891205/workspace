package com.java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.java.Service.BoardService;
import com.java.dto.BoardDto;

@Controller
public class BoardController {

	@Autowired
	BoardService boardService;

	@GetMapping("/board/blist")
	public String blist(Model model) {
		List<BoardDto> list = boardService.SelectAll();
		model.addAttribute("list", list);
		System.out.println("list개수 : " + list.size());
		return "blist";
	}
}