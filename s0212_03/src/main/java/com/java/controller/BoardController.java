package com.java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.java.Service.BoardService;
import com.java.dto.BoardDto;

@Controller
public class BoardController {

	@Autowired
	BoardService boardService;

	@GetMapping("/write")
	// 글쓰기 폼
	public String writeForm() {
		return "board/write";
	}

	@PostMapping("/write")
	public String writeSubmit(BoardDto boardDto) {
		// 글쓰기 처리
		return "redirect:/board/blist";
	}

	@GetMapping("/board/blist")
	public String blist(Model model) {
		// 게시글 전체가져오기 - 여러개
		List<BoardDto> list = boardService.selectAll();
		model.addAttribute("list", list);
		System.out.println("list 개수 :" + list.size());
		return "blist";
	}
}
