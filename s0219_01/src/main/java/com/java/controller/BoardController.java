package com.java.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.java.dto.BoardDto;
import com.java.service.BoardService;

import jakarta.servlet.http.HttpSession;

@Controller
public class BoardController {

	private final FController FController;

	@Autowired
	BoardService boardService;

	@Autowired
	HttpSession session;

	// 답변달기-----------------------------------------------
	@GetMapping("/board/breply") // 답변달기
	public String breply(BoardDto boardDto, Model model) {
		BoardDto bdto = boardService.selectOne(boardDto);
		model.addAttribute("bdto", bdto);
		return "board/breply";
	}

	// 답변달기
	@PostMapping("/board/breply") // 답변달기 저장
	public String dobreply(BoardDto boardDto) {
		String id = (String) session.getAttribute("session_id");
		boardDto.setId(id);
		boardService.InsertReply(boardDto);
		return "redirect:/board/breply/blist";
	}// ------------------------------------------------------

	@PostMapping("/board/bupdate") // 수정 저장
	public String dobupdate(
		@RequestParam(value = "bno", required = false, defaultValue = "0") int bno,
		@RequestParam(value = "btitle", required = false, defaultValue = "") String btitle,
		@RequestParam(value = "bcontent", required = false, defaultValue = "") String bcontent,
		@RequestParam(value = "bfile", required = false) String bfile) {
		
		// bno 값 검증
		if (bno <= 0) {
			return "redirect:/board/blist";
		}
		
		// 기존 게시글 데이터 조회
		BoardDto existingBoard = boardService.selectOne(bno);
		if (existingBoard == null) {
			return "redirect:/board/blist";
		}
		
		// 로그인 사용자 확인
		String id = (String) session.getAttribute("session_id");
		if (id == null || !id.equals(existingBoard.getId())) {
			return "redirect:/member/login";
		}
		
		// 필요한 필드만 업데이트
		existingBoard.setBtitle(btitle);
		existingBoard.setBcontent(bcontent);
		if (bfile != null && !bfile.isEmpty()) {
			existingBoard.setBfile(bfile);
		}
		
		// 업데이트 실행
		boardService.updateBoard(existingBoard);
		return "redirect:/board/blist?flag=2";
	}

	@GetMapping("/board/bupdate") // 수정 페이지 열기
	public String bupdate(BoardDto boardDto, Model model) {
		BoardDto bdto = boardService.selectOne(boardDto);
		model.addAttribute("bdto", bdto);
		return "board/bupdate";
	}

	// @PutMapping("/board/bdelete") // 삭제 Method전송방식
	@GetMapping("/board/bdelete")
	public String bdelete(@RequestParam(name = "bno", defaultValue = "1") int bno) {
		String id = (String) session.getAttribute("session_id");
		BoardDto bdto = boardService.selectOne(bno);
		if (id == null || !id.equals(bdto.getId())) {
			return "redirect:/member/login";
		}
		boardService.deleteBoard(bno, id);
		return "redirect:/board/blist?flag=3";
	}

	@GetMapping("/board/bview") // 게시글 상세보기
	public String bview(BoardDto boardDto, Model model) {
		System.out.println("bview bno : " + boardDto.getBno());
		// 1개 가져오기
		BoardDto bDto = boardService.selectOne(boardDto);
		model.addAttribute("board", bDto);
		return "board/bview";
	}

	BoardController(FController FController) {
		this.FController = FController;
	}

	@GetMapping("/board/blist") // 게시글 전체가져오기
	public String blist(@RequestParam(value = "flag", required = false) String flag, Model model) {
		List<BoardDto> list = boardService.selectAll();
		model.addAttribute("flag", flag);
		model.addAttribute("list", list);
		return "board/blist";
	}

	@GetMapping("/board/bwrite") // 글쓰기 페이지 열기
	public String bwrite() {
		return "board/bwrite";
	}

	@PostMapping("/board/bwrite") // 글쓰기 저장
	public String bwrite(BoardDto boardDto, Model model) {
		String id = (String) session.getAttribute("session_id");
		if (id == null || id.isBlank()) {
			return "redirect:/member/login?flag=2";
		}
		boardDto.setId(id);
		System.out.println("제목 : " + boardDto.getBtitle());
		boardService.insertBoard(boardDto);

		return "redirect:/board/blist?flag=1";
	}
}