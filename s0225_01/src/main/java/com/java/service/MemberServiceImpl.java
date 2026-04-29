package com.java.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.MemberDto;
import com.java.repository.MemberRepository;

import jakarta.transaction.Transactional;

@Service
public class MemberServiceImpl implements MemberService {

	@Autowired
	MemberRepository memberRepository;

	@Override // 로그인 확인
	public MemberDto findByIdAndPw(MemberDto mdto) {
		System.out.println("service mdto : " + mdto.getId());

		// findByIdAndPw
		// select * from memberDto where id =? and pw=?
		// findByNameOrPhone -> select * from memberDto where name=? or phone=?
		// findByNonBetween(1,10) -> select * from memberDto where num between 1 and 10
		// select 1개일때 -> null에 대한 처리를 해줘야 함.
		// 1. .get() : 에러처리를 하지 않음
		// 2. .orElse(null) : null에 대한 처리, 빈객체로 처리
		// 3. .orElseThrow() : 에러처리를 함. 람다식으로 처리
//		MemberDto memberdto = memberRepository.findByIdAndPw(mdto.getId(), mdto.getPw())
//				.orElseThrow(() -> {
//			return new IllegalArgumentException();
//		});
//				.get();
//				.orElse(null);
//				.orElse(new MemberDto());
		// 지정하는 이름방식을 따르지 않을 경우
		MemberDto memberDto = memberRepository.selectLogin(mdto.getId(), mdto.getPw()).orElse(null);
		return memberDto;
	}// 로그인 확인

	@Override // 전체회원리스트
	// select : 여러개 데이터를 가져오는 경우, null 처리를 할 필요가 없음.
	// List타입 : null을 받아도 됨.
	public List<MemberDto> findAll() {
		// findAll() : MemberRepository 메소드선언 할 필요가 없음.
		List<MemberDto> list = memberRepository.findAll();
		return list;
	}

	@Override // 회원삭제
	public void deleteById(MemberDto mdto) {
		memberRepository.deleteById(mdto.getId());

	}

	@Override // 회원가입저장,수정
	@Transactional
	public void save(MemberDto mdto) {
		memberRepository.save(mdto);
	}

	@Override // 회원정보 상세보기
	public MemberDto findById(MemberDto mdto) {
		MemberDto memberDto = memberRepository.findById(mdto.getId()).orElse(null);
		return memberDto;
	}

	@Transactional
	@Override // 회원정보 수정저장
	public void update(MemberDto mdto) {
		// 수정1. 검색 후 검색된 데이터에 갑변경
		// 아이디,패스워드,이름,폰,이메일,성별,취미
		// 패스워드,폰,이메일,성별,취미
		// 폰,이메일,성별,취미만 수정가능
//		MemberDto memberDto = memberRepository.findById(mdto.getId()).orElse(null);
//		memberDto.setPhone(mdto.getPhone());
//		memberDto.setEmail(mdto.getEmail());
//		memberDto.setGender(mdto.getGender());
//		memberDto.setHobby(mdto.getHobby());

		// 수정2. save() : 아이디가 없으면 insert, 아이디가 있으면 update진행
		memberRepository.save(mdto);

	}

}
