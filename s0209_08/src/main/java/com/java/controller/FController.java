package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import jakarta.servlet.http.HttpServletRequest;

@Controller
public class FController {
	
	public String index() {
		return "index";		
	}
	
	// list 출력
	@GetMapping("/list")
	public String list() {
		return "list";		
	}
	
	@GetMapping("/member/member")
	public String member() {
		return "member";		
	}
	

	@PostMapping("/member/member") // 오버로딩 : 메소드명은 같고 , 매개변수개수 타입이 다른것
	public ModelAndView member(HttpServletRequest request,Model model) { // 오버로딩 -> 같은 이름의 메서드
		// 데이터 받기
		String id = request.getParameter("id");
		
		// 데이터 보내기
		ModelAndView mv = new ModelAndView();
		mv.addObject("id", id);
		mv.setViewName("memberOk");
		
		return mv;		
	}
	
	// Model model 방식
//	@PostMapping("/member/member") // 오버로딩 : 메소드명은 같고 , 매개변수개수 타입이 다른것
//	public String member(HttpServletRequest request,Model model) { // 오버로딩 -> 같은 이름의 메서드
//		// 데이터 받기
//		String id = request.getParameter("id");
//		
//		// 데이터 보내기
//		model.addAttribute("id", id);
//		
//		// 콘솔에 출력
//		System.out.println("넘어온 데이터 : " + id);
//		return "memberOk";		
//	}
	
	
	
	@GetMapping("/member/login")
	public String login() {
		return "login";		
	}
	
	@PostMapping("/member/loginOk")
	public String loginOk(HttpServletRequest request,Model model) {
		// 데이터 받기
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		// checkbox -> getParameterValues();
		System.out.println("넘어온데이터 : " + id+", "+pw);
		// 데이터 보내기
		model.addAttribute("id", id);
		model.addAttribute("pw", pw);
		return "loginOk";		
	}
	
	// /member/membershipOk 출력
	@PostMapping("/member/membershipOk")
	public String membershipOk(HttpServletRequest request,
			HttpServletRequest response,Model model) {
		// 데이터 받기
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		String name = request.getParameter("name");
		String phone = request.getParameter("phone");
		String email = request.getParameter("email");
		String[] hobbies = request.getParameterValues("hobby");
		String hobbyStr = "";
		if (hobbies != null && hobbies.length > 0) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < hobbies.length; i++) {
				sb.append(hobbies[i]);
				if (i < hobbies.length - 1) sb.append(", ");
			}
			hobbyStr = sb.toString();
		}
		// gender 체크박스 처리
		String[] genders = request.getParameterValues("gender");
		String genderStr = "";
		if (genders != null && genders.length > 0) {
			StringBuilder sbg = new StringBuilder();
			for (int i = 0; i < genders.length; i++) {
				sbg.append(genders[i]);
				if (i < genders.length - 1) sbg.append(", ");
			}
			genderStr = sbg.toString();
		}
		// 콘솔에 출력
		System.out.println("넘어온 데이터 -> id:" + id + ", pw:" + pw + ", name:" + name + ", phone:" + phone + ", email:" + email + ", gender:" + genderStr + ", hobby:" + hobbyStr);
		// 데이터 보내기
		model.addAttribute("id", id);
		model.addAttribute("pw", pw);
		model.addAttribute("name", name);
		model.addAttribute("phone", phone);
		model.addAttribute("email", email);
		model.addAttribute("hobby", hobbyStr);
		model.addAttribute("gender", genderStr);
		return "membershipOk";
	}
	
	@GetMapping("/member/membership")
	public String membership() {
        return "membership";
    }
}