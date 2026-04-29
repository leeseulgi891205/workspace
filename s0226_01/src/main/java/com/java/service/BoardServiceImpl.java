package com.java.service;

import java.sql.Timestamp;
import java.util.HashMap; // 추가됨
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.java.dto.BoardDto;
import com.java.repository.BoardRepository;

@Service
public class BoardServiceImpl implements BoardService {

	@Autowired
	private BoardRepository boardRepository;

	@Override // 게시글 전체 조회
	public List<BoardDto> findAll(Sort sort) {
		return boardRepository.findAll(sort);
	}

	@Transactional // 글쓰기 저장
	@Override
	public void save(BoardDto bdto) {
		// 1. 먼저 저장하여 시퀀스(bno)를 생성합니다.
		BoardDto boardDto = boardRepository.save(bdto);
		// 2. 생성된 bno를 bgroup에 설정합니다.
		boardDto.setBgroup(boardDto.getBno());
		// @Transactional에 의해 메서드 종료 시 변경사항이 DB에 더티 체킹으로 반영됩니다.
	}

	@Transactional // 게시글 수정 저장
	@Override
	public void update(BoardDto bdto) {
		// Optional 처리를 통해 NullPointerException 방지
		BoardDto boardDto = boardRepository.findById(bdto.getBno())
				.orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

		boardDto.setBtitle(bdto.getBtitle());
		boardDto.setBcontent(bdto.getBcontent());
		boardDto.setBfile(bdto.getBfile());
		boardDto.setBdate(new Timestamp(System.currentTimeMillis()));
	}

	@Transactional // 답변달기 저장
	@Override
	public void reply(BoardDto bdto) {
		// 1. 기존 답변들의 순서(bstep) 조정
		boardRepository.replyBstepUP(bdto.getBgroup(), bdto.getBstep());

		// 2. 답변 데이터 설정 (부모보다 1씩 증가)
		bdto.setBstep(bdto.getBstep() + 1);
		bdto.setBindent(bdto.getBindent() + 1);

		boardRepository.save(bdto);
	}

	@Transactional(readOnly = true) // 게시글 상세 보기 및 조회수 증가
	@Override
	public Map<String, Object> findById(Integer bno) {
		Map<String, Object> map = new HashMap<>();

		// 1. 현재 게시글 가져오기 및 조회수 증가
		BoardDto boardDto = boardRepository.findById(bno).orElseThrow(() -> new RuntimeException("게시글이 존재하지 않습니다."));
		boardDto.setBhit(boardDto.getBhit() + 1); // 조회수 증가

		// 2. 이전글/다음글 가져오기
		BoardDto preDto = boardRepository.findByPre(bno).orElse(null);
		BoardDto nextDto = boardRepository.findByNext(bno).orElse(null);

		map.put("boardDto", boardDto);
		map.put("preDto", preDto);
		map.put("nextDto", nextDto);

		return map;
	}

	@Override // 게시글 삭제
	public void deleteById(Integer bno) {
		boardRepository.deleteById(bno);
	}
}
