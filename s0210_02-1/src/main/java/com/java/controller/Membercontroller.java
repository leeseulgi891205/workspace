package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.java.Dto.MemberDto;

import jakarta.servlet.http.HttpServletRequest;

@Controller
public class Membercontroller {

	@GetMapping("/login")
	public String login() {
		return "login";
	}

	@PostMapping("/login")
	public String doLogin(MemberDto member, Model model, HttpServletRequest request) {
		// null-safe retrieval
		String id = member != null && member.getId() != null ? member.getId() : "";
		String pw = member != null && member.getPw() != null ? member.getPw() : "";
		System.out.println("id : " + id);
		System.out.println("pw : " + pw);

		if ("aaa".equals(id) && "1111".equals(pw)) {
			// store logged-in user in session
			request.getSession().setAttribute("member", member);
			// redirect to index
			return "redirect:/";
		} else {
			model.addAttribute("msg", "아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요.");
			return "redirect:/login?fail=2";

		}

	}

	@GetMapping({"/mUpdate", "/mupdate"})
	public String mUpdateForm(HttpServletRequest request, Model model) {
		Object m = request.getSession().getAttribute("member");
		if (m != null && m instanceof MemberDto) {
			model.addAttribute("member", (MemberDto) m);
			return "mupdate";
		} else {
			// not logged in, redirect to login
			return "redirect:/login";
		}
	}

	@PostMapping({"/mUpdate", "/mupdate"})
	public String mupdateSubmit(MemberDto formMember, HttpServletRequest request, Model model) {
		Object m = request.getSession().getAttribute("member");
		if (m != null && m instanceof MemberDto) {
			MemberDto sessionMember = (MemberDto) m;
			// update allowed fields
			sessionMember.setName(formMember.getName());
			sessionMember.setEmail(formMember.getEmail());
			sessionMember.setPhone(formMember.getPhone());
			sessionMember.setGender(formMember.getGender());
			sessionMember.setHobby(formMember.getHobby());
			// save back to session
			request.getSession().setAttribute("member", sessionMember);
			model.addAttribute("member", sessionMember);
			return "mupdate"; // show updated member info
		} else {
			return "redirect:/login";
		}
	}

	@GetMapping("/join")
	public String join() {
		return "join";
	}

	@PostMapping("/join")
	public String join(MemberDto member, Model model) {
		System.out.println("회원가입 확인: " + member);
		model.addAttribute("member", member);
		return "dojoin";
	}
}