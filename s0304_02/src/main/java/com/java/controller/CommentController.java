package com.java.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.java.dto.CommentDto;
import com.java.service.CommentService;

import jakarta.servlet.http.HttpSession;

@Controller
public class CommentController {

	@Autowired
	CommentService commentService;
	@Autowired
	HttpSession session;

	@ResponseBody // 페이지 리턴할 것이 아니기 때문에 꼭 붙여야 함
	@PostMapping("/comment/save")
	public CommentDto save(CommentDto cdto, @RequestParam(name = "bno", defaultValue = "1") int bno,
			@RequestParam(name = "day", defaultValue = "1") String day) {
		System.out.println("controller ccontent : " + cdto.getCcontent());
		System.out.println("controller cno : " + cdto.getCno());
		System.out.println("controller day : " + day);
		System.out.println("controller bno : " + bno);
		// service 전달
		// CommentDto commentDto = commentService.save(cdto,bno);

		CommentDto commentDto = new CommentDto(); // 객체선언 -> 빈 객체 넘어감

		return commentDto;
	}

	@PostMapping("/comment/save2")
	@ResponseBody
	public String save2(CommentDto cdto, @RequestParam(name = "bno", defaultValue = "1") int bno,
			@RequestParam(name = "day", defaultValue = "1") String day) {
		System.out.println("ccontent : " + cdto.getCcontent());
		System.out.println("bno : " + bno);
		System.out.println("cno : " + cdto.getCno());
		System.out.println("cdate : " + cdto.getCdate());

		CommentDto commentDto = new CommentDto();

		return "commentDto";
	}

}
