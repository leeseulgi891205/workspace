package com.java.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.java.dto.TraineeDTO;

@Controller
public class MainController {

	@GetMapping("/")
	public String index() {
		return "redirect:/main";
	}

	@GetMapping("/main")
	public String mainPage(Model model) {
		// 실제로는 DB에서 연습생 데이터를 가져와야 합니다.
		List<TraineeDTO> trainees = new ArrayList<>();
		trainees.add(new TraineeDTO("민지", "청량", 90, 85, "minji.jpg"));
		trainees.add(new TraineeDTO("제이", "힙합", 80, 95, "jay.jpg"));
		trainees.add(new TraineeDTO("하니", "발라드", 95, 88, "hani.jpg"));
		trainees.add(new TraineeDTO("다니엘", "댄스", 88, 92, "daniel.jpg"));
		trainees.add(new TraineeDTO("해린", "청량", 92, 87, "haerin.jpg"));
		trainees.add(new TraineeDTO("허재", "록", 87, 91, "taeyang.jpg"));
		trainees.add(new TraineeDTO("철수", "힙합", 83, 94, "junho.jpg"));
		trainees.add(new TraineeDTO("도라에몽", "발라드", 93, 86, "minsu.jpg"));
		trainees.add(new TraineeDTO("만득", "댄스", 85, 96, "hyunwoo.jpg"));
		trainees.add(new TraineeDTO("덕팔", "청량", 89, 88, "jihoon.jpg"));

		model.addAttribute("traineeList", trainees);
		return "main"; // main.jsp 또는 main.html로 이동
	}
}
