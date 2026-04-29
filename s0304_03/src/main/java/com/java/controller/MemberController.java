package com.java.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.java.dto.MemberDto;

import jakarta.servlet.http.HttpSession;

@Controller
public class MemberController {

	@Autowired
	HttpSession session;

	// 회원가입페이지
	@GetMapping("/member/memberShip") // get으로 회원가입 페이지 열기
	public String memberShip() {
		return "memberShip";
	}

	// 회원가입저장
	@ResponseBody // 페이지 리턴할 것이 아니기 때문에 꼭 붙여야 함
	@PostMapping("/member/memberShip") // post로 회원가입 진행
	public String memberShip(MemberDto mdto, @RequestParam(name = "bno", required = false) Integer bno, Model model) {

		System.out.println("bno : " + bno);
		System.out.println("id : " + mdto.getId());
		System.out.println("pw : " + mdto.getPw());

//		return "redirect:/member/mlist";
		return "성공";
	}

}
