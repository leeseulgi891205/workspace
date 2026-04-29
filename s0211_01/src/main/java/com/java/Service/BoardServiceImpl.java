package com.java.Service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.BoardDto;
import com.javaDao.BoardDao;

@Service // 객체선언없이 사용가능
public class BoardServiceImpl implements BoardService {

	@Autowired
	BoardDao boardDao;

	@Override
	public List<BoardDto> SelectAll() {
		// MyBatis에서 Dao로 사용할 인터페이스에 @Mapper 어노테이션을 붙이면, 해당 인터페이스의 메소드명과 동일한 id를 가진
		// SQL문이 매핑되어 실행된다.
		List<BoardDto> list = boardDao.SelectAll();

//		List<BoardDto> list = new ArrayList<>();
//		list.add(new BoardDto(1, "제목1", "내용1", "aaa", 1, 0, 0, 0, null, new Timestamp(System.currentTimeMillis()),
//				new Timestamp(System.currentTimeMillis())));
//		list.add(new BoardDto(1, "제목2", "내용2", "aaa", 2, 0, 0, 0, null, new Timestamp(System.currentTimeMillis()),
//				new Timestamp(System.currentTimeMillis())));

		return list;
	}

}
