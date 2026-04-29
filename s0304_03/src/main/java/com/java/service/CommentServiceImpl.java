package com.java.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.BoardDto;
import com.java.dto.CommentDto;
import com.java.dto.MemberDto;
import com.java.repository.CommentRepository;

import jakarta.servlet.http.HttpSession;

@Service
public class CommentServiceImpl implements CommentService {

	@Autowired
	CommentRepository commentRepository;

	@Autowired
	MemberService memberService;

	@Autowired
	BoardService boardService;

	@Autowired
	HttpSession session;

	// 하단댓글저장
	@Override
	public CommentDto save(CommentDto cdto, int bno) {
		String id = (String) session.getAttribute("session_id");
		MemberDto mdto = memberService.findById(id);
		BoardDto bdto = (BoardDto) boardService.findById(bno).get("boardDto");
		cdto.setMemberDto(mdto);
		cdto.setBoardDto(bdto);
		// db에 저장
		// cno자동,ccontent입력, boardDto검색, memberDto검색, cdate자동
		CommentDto commentDto = commentRepository.save(cdto);
		return commentDto;
	}

}
