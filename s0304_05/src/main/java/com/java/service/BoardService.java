package com.java.service;

import java.util.List;
import java.util.Map;

import com.java.dto.BoardDto;

public interface BoardService {
	
	Map<String, Object> findById(Integer bno);
	
	Map<String, Object> findAll(int page, int size, String category, String search);
	
	void save(BoardDto bdto);
	
	void update(BoardDto bdto);
	
	void reply(BoardDto bdto);
	
	void deleteById(Integer bno);
}
