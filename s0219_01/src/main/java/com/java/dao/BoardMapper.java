package com.java.dao;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.java.dto.BoardDto;

@Mapper
public interface BoardMapper {

	// 게시글 전체가져오기 - boardMapper.xml
	List<BoardDto> selectAll();

	// 게시글 쓰기
	void insertBoard(BoardDto boardDto);

	// 게시글 1개 가져오기
	BoardDto selectOne(int bno);

	void deleteBoard(int bno);

	void updateBoard(BoardDto boardDto);

	// 답변달기 같은 bgroup 모두 bstep1증가
	void updateReply(BoardDto boardDto);

	// 답변달기 저장
	void insertReply(BoardDto boardDto);

}
