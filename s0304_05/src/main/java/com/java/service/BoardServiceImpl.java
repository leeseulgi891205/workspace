package com.java.service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.BoardDto;
import com.java.repository.BoardRepository;

@Service
public class BoardServiceImpl implements BoardService {
	
	@Autowired
	BoardRepository boardRepository;

	@Override
	public Map<String, Object> findById(Integer bno) {
		Map<String, Object> map = new HashMap<>();
		BoardDto boardDto = boardRepository.findById(bno).orElse(null);
		map.put("boardDto", boardDto);
		map.put("preDto", null);
		map.put("nextDto", null);
		return map;
	}

	@Override
	public Map<String, Object> findAll(int page, int size, String category, String search) {
		Map<String, Object> map = new HashMap<>();
		List<BoardDto> list = boardRepository.findAll();
		map.put("list", list);
		map.put("totalCount", list.size());
		map.put("page", page);
		map.put("size", size);
		return map;
	}

	@Override
	public void save(BoardDto bdto) {
		boardRepository.save(bdto);
	}

	@Override
	public void update(BoardDto bdto) {
		boardRepository.save(bdto);
	}

	@Override
	public void reply(BoardDto bdto) {
		boardRepository.save(bdto);
	}

	@Override
	public void deleteById(Integer bno) {
		boardRepository.deleteById(bno);
	}

}
