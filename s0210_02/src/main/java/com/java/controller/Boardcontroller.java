package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.java.dto.BoardDto;

@Controller
public class Boardcontroller {

	@GetMapping("/board")
	public String board() {
		return "board";
	}

	// 4. 객체타입 방식
	@PostMapping("/board")
	public String board(BoardDto bdto, Model model) {
		model.addAttribute("board", bdto);
		return "doboard";
	}

	// 3. 축약방식
	// @RequestParam 방식 - 이름이 같으면 이름 생략가능
	// 자동으로 형변환 가능 - 타입이 다른경우는 null값일때 에러발생
	// 타입변경시 null값 입력될때, 디폴드값 설정가능
//	@PostMapping("/board")
//	public String board(@RequestParam(name = "bno", defaultValue = "1") int bno, String btitle, String bcontent,
//			String id, Model model) {
//		System.out.println(String.format("%d,%s,%s,%s", bno, btitle, bcontent, id));
//		model.addAttribute("bno", bno);
//		model.addAttribute("btitle", btitle);
//		model.addAttribute("bcontent", bcontent);
//		model.addAttribute("id", id);
//
//		return "doboard";
//	}

//	// 2. @RequestParam 방식
//	@PostMapping("/board")
//	public String board(@RequestParam("bno") String bno,
//						@RequestParam("btitle") String btitle,
//						@RequestParam("bcontent") String bcontent,
//						@RequestParam("id") String id,
//			Model model) {
//		System.out.println(String.format("bno: %s, btitle: %s, bcontent: %s, id: %s", 
//		bno, btitle, bcontent, id));
//		model.addAttribute("bno", bno);
//		model.addAttribute("btitle", btitle);
//		model.addAttribute("bcontent", bcontent);
//		model.addAttribute("id", id);
//		
//		
//		return "doboard";
//	}

	// 1. HttpServletRequest request 방식
//	@PostMapping("/board")
//	public String board(HttpServletRequest request, Model model) {
//		int bno = Integer.parseInt(request.getParameter("bno"));
//		String btitle = request.getParameter("btitle");
//		String bcontent = request.getParameter("bcontent");
//		String id = request.getParameter("id");
//		System.out.println(String.format("bno: %s, btitle: %s, bcontent: %s, id: %s", 
//				bno, btitle, bcontent, id));
//		model.addAttribute("bno", bno);
//		model.addAttribute("btitle", btitle);
//		model.addAttribute("bcontent", bcontent);
//		model.addAttribute("id", id);
//		return "doboard";
//	}
}
