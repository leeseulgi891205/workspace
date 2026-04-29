package com.java.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.java.dto.BoardDto;
import com.java.repository.BoardRepository;

@Service
public class BoardServiceImpl implements BoardService {

	@Autowired
	BoardRepository boardRepository;

	@Override // 게시글 전체 조회
	public List<BoardDto> findAll(Sort sort) {
		List<BoardDto> list = boardRepository.findAll(sort);
		return list;
	}

	@Transactional // 트랜잭션 처리 - 메소드 완료시 기존의 연속성context가 수정되면 db에 자동반영
	@Override // 글쓰기 저장
	public void save(BoardDto bdto) {
		// Repository에 저장시 객체를 리턴해줌.
		BoardDto boardDto = boardRepository.save(bdto);
		// bgroup에 bno번호를 다시 넣어줌.
		boardDto.setBgroup(boardDto.getBno()); // 글쓰기 저장 후 bgroup에 bno값을 저장
//		boardRepository.save(boardDto); // @Transactional 있으면 생략가능

	}

	@Override // 게시글 1개 가져오기
	public BoardDto findById(Integer bno) {
		BoardDto boardDto = boardRepository.findById(bno).orElse(null);
		return boardDto;
	}

}
