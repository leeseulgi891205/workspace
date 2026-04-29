package com.java.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.java.dto.MemberDto;
import com.java.repository.MemberRepository;

@Service
public class MemberServiceImpl implements MemberService {
	
	@Autowired
	MemberRepository memberRepository;

	@Override
	public MemberDto findById(String id) {
		return memberRepository.findById(id).orElse(null);
	}

	@Override
	public MemberDto findByIdAndPw(MemberDto mdto) {
		return memberRepository.findByIdAndPw(mdto.getId(), mdto.getPw());
	}

	@Override
	public List<MemberDto> findAll() {
		return memberRepository.findAll();
	}

	@Override
	public void save(MemberDto mdto) {
		memberRepository.save(mdto);
	}

	@Override
	public void update(MemberDto mdto) {
		memberRepository.save(mdto);
	}

	@Override
	public void deleteById(MemberDto mdto) {
		memberRepository.deleteById(mdto.getId());
	}

}
