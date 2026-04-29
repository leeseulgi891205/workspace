package com.java.service;

import com.java.dto.CommentDto;

public interface CommentService {

	// 댓글저장
	CommentDto save(CommentDto cdto, int bno);

}
