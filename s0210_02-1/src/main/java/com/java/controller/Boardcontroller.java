package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.java.Dto.BoardDto;

@Controller
public class Boardcontroller {

	public ModelAndView boardView(@PathVariable Integer bno) {
		BoardDto b = BoardDto.builder().bno(bno).btitle("게시글제목").bcontent("게시글내용").id("작성자ID").build();

		ModelAndView mv = new ModelAndView();
		mv.addObject("bno", bno);
		mv.setViewName("boardView");
		return mv;
	} // boardModelAndView

	@GetMapping("/board")
	public String board() {
		return "board";
	} // board form

	@PostMapping("/board")
	public String board(BoardDto board, Model model) {
		System.out.println("게시글등록 확인: " + board);
		model.addAttribute("board", board);
		return "doboard";
	} // board

	@GetMapping("/boardView")
	public String boardView() {
		return "boardView";
	}
}