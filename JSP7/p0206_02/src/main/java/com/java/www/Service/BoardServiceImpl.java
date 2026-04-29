package com.java.www.Service;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.java.www.Dao.BoardDao;
import com.java.www.Dto.BoardDto;
import java.util.List;

public class BoardServiceImpl implements BoardService {

    @Override
    public void execute(HttpServletRequest request, HttpServletResponse response) {
        // 게시판 목록 조회
        BoardDao boardDao = new BoardDao();
        List<BoardDto> boardList = boardDao.selectAllBoards();
        
        // request에 게시판 목록 저장
        request.setAttribute("boardList", boardList);
    }
}