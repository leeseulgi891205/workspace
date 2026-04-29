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

	@Override // 전체게시글리스트 - 하단넘버링(현재페이지, 페이지당개수)
	public Map<String, Object> findAll(int page, int size, String category, String search) {

		// 정렬 - bgroup:역순정렬,bstep:순차정렬
		Sort sort = Sort.by(Sort.Order.desc("bgroup"), Sort.Order.asc("bstep"));
		// Pageable 0부터 시작 1페이지가 0페이지가 됨.
		Pageable pageable = PageRequest.of(page - 1, size, sort);
		// Repository로 전달해서 db가져옴.
		Page<BoardDto> pageList = null;
		// 검색이 아닐경우
		if (category == null || category == "") {
			pageList = boardRepository.findAll(pageable);
		} else {
			if (category.equals("all")) {
				pageList = boardRepository.findByBtitleContainingOrBcontentContaining(search, search, pageable);
			} else if (category.equals("btitle")) {
				pageList = boardRepository.findByBcontentContaining(search, pageable);
			} else if (category.equals("bcontent")) {
				pageList = boardRepository.findByBcontentContaining(search, pageable);
			}
		}

		List<BoardDto> list = pageList.getContent();
		int maxPage = pageList.getTotalPages();
		int startPage = ((page - 1) / 5) * 5 + 1; // 0-10:1, 11-20:11
		int endPage = Math.min(startPage + 5 - 1, maxPage); // 0-10:10, 11-20:20
//		if (endPage > maxPage) {
//			endPage = maxPage;
//		}
		Map<String, Object> map = new HashMap<>();
		map.put("list", list); // 게시글 데이터
		map.put("maxPage", maxPage); // 최대 페이지
		map.put("startPage", startPage); // 하단넘버링 시작번호
		map.put("endPage", endPage); // 하단넘버링 끝번호
		map.put("page", page); // 현재 페이지
		map.put("category", category); // 검색카테고리
		map.put("search", search); // 검색어

		return map;
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
