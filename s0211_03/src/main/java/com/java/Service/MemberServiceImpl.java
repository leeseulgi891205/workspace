package com.java.Service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.MemberDto;
import com.javaDao.MemberDao;

@Service
public class MemberServiceImpl implements MemberService {

	@Autowired
	MemberDao memberDao;

	@Override // 전체 회원 조회
	public List<MemberDto> selectAll() {
		return memberDao.selectAll();
	}

}
