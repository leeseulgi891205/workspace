package com.java.service;

import java.sql.Timestamp;
import java.util.HashMap; // 추가됨
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.java.dto.BoardDto;
import com.java.repository.BoardRepository;

@Service
public class BoardServiceImpl implements BoardService {

	@Autowired
	private BoardRepository boardRepository;

	// 전체게시글리스트 - pageable
	@Override
	public Map<String, Object> findAll(int page, int size) {
		Sort sort = Sort.by(Sort.Order.desc("bgroup"), Sort.Order.asc("bstep"));
		Pageable pageable = PageRequest.of(page - 1, size, sort);
		Page<BoardDto> pageList = boardRepository.findAll(pageable);
		// 일반적인 형태
//		List<BoardDto> list = boardRepository.findAll();

		// 하단넘버링에 필요한 페이지를 구함.
		int maxPage = pageList.getTotalPages(); // 마지막페이지
		int startPage = ((page - 1) / 10) * 10 + 1; // 하단넘버링 시작번호
		int endPage = Math.min(startPage + 10 - 1, maxPage); // 하단넘버링 마지막번호
		List<BoardDto> list = pageList.getContent(); // 게시글내용
		Map<String, Object> map = new HashMap<>();
		map.put("page", page); // 화면 페이지 번호(1부터 시작)
		map.put("maxPage", maxPage);
		map.put("startPage", startPage);
		map.put("endPage", endPage);
		map.put("list", list);
		// 하단넘버링에 필요한 데이터

		return map;
	} // blist-pageable

	// 글쓰기 저장
	@Transactional
	@Override
	public void save(BoardDto bdto) {
		// 1. 먼저 저장하여 시퀀스(bno)를 생성합니다.
		BoardDto boardDto = boardRepository.save(bdto);
		// 2. 생성된 bno를 bgroup에 설정합니다.
		boardDto.setBgroup(boardDto.getBno());
		// @Transactional에 의해 메서드 종료 시 변경사항이 DB에 더티 체킹으로 반영됩니다.
	}

	// 게시글 수정 저장
	@Transactional
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

	// 답변달기 저장
	@Transactional
	@Override
	public void reply(BoardDto bdto) {
		// 1. 기존 답변들의 순서(bstep) 조정
		boardRepository.replyBstepUP(bdto.getBgroup(), bdto.getBstep());

		// 2. 답변 데이터 설정 (부모보다 1씩 증가)
		bdto.setBstep(bdto.getBstep() + 1);
		bdto.setBindent(bdto.getBindent() + 1);

		boardRepository.save(bdto);
	}

	// 게시글 상세 보기 및 조회수 증가
	@Transactional(readOnly = true)
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
