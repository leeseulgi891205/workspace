package com.java.www.service;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.java.www.Dao.BoardDao;
import com.java.www.Dto.BoardDto;

public class BoardServiceImpl implements BoardService {
	
	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) {
		BoardDao bdao = new BoardDao();
		List<BoardDto> list = bdao.boardList();
		
		System.out.println("=== BoardServiceImpl Debug ===");
		System.out.println("BoardServiceImpl - board list size: " + list.size());
		
		if (list.size() > 0) {
			for (BoardDto board : list) {
				System.out.println("Board No: " + board.getNo() + ", Title: " + board.getTitle() + ", Writer: " + board.getWriter());
			}
		} else {
			System.out.println("게시판 데이터가 없습니다. DB에 board 테이블과 데이터를 확인하세요.");
		}
		
		request.setAttribute("boardList", list);
	}
}
