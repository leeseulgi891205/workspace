package com.java.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.BoardDto;
import com.java.dto.CommentDto;
import com.java.repository.BoardRepository;
import com.java.repository.CommentRepository;

@Service
public class CommentServiceImpl implements CommentService {
	
	@Autowired
	CommentRepository commentRepository;
	
	@Autowired
	BoardRepository boardRepository;

	@Override
	public CommentDto save(CommentDto cdto, int bno) {
		BoardDto boardDto = boardRepository.findById(bno).orElse(null);
		cdto.setBoardDto(boardDto);
		return commentRepository.save(cdto);
	}

}
