package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.java.dto.NoticeDTO;

@Controller
public class NoticeController {

	// 공지사항 목록 화면 이동
	@GetMapping("/board/notice")
	public String noticeList() {
		return "notice"; // WEB-INF/views/notice.jsp 화면을 띄워라
	}

	// 글쓰기 화면 이동
	@GetMapping("/board/noticeWrite")
	public String noticeWriteForm() {
		return "noticeWrite"; // WEB-INF/views/noticeWrite.jsp 화면을 띄워라
	}

	// 글쓰기 처리
	@PostMapping("/board/noticeWrite")
	public String noticeWrite(NoticeDTO noticeDTO) {
		System.out.println("제목: " + noticeDTO.getTitle());
		// DB 저장 로직 추가 위치

		// 글 작성 완료 후 다시 목록으로 리다이렉트 (주소 주의!)
		return "redirect:/board/notice";
	}
}
