package com.java.service;

import java.util.List;
import java.util.Map;

import com.java.dto.BoardDto;
import com.java.dto.searchDto;

public interface BoardService {

	// 게시글 전체가져오기
	Map<String, Object> selectAll();

	// 검색
	List<BoardDto> selectSearch(searchDto searchDto);

	// 게시글 1개가져오기
	BoardDto selectOne(BoardDto boardDto);

	// 게시글수정 및 1개가져오기
	BoardDto updateBoard(BoardDto boardDto);

	// 게시글쓰기
	void insertBoard(BoardDto boardDto);

	// 답변달기 저장
	void InsertReply(BoardDto boardDto);

	// 게시글 삭제
	void deleteBoard(BoardDto boardDto);

	// 게시글 전체가져오기 페이징
	Map<String, Object> selectAll(int page);

}
