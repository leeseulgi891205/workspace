package com.java.service;

import java.util.List;

import org.springframework.data.domain.Sort;

import com.java.dto.BoardDto;

public interface BoardService {

	// 게시글 전체 조회
	List<BoardDto> findAll(Sort sort);

	// 글쓰기 저장
	void save(BoardDto bdto);

	// 게시글 1개 가져오기
	BoardDto findById(Integer bno);

}
