package com.java.controller;

import java.util.Arrays;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.servlet.http.HttpServletRequest;

@Controller
public class Membercontroller {

    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @PostMapping("/login")
    public String login(HttpServletRequest request, Model model) {
        String id = request.getParameter("id");
        String pw = request.getParameter("pw");
        System.out.println("id: " + id);
        System.out.println("pw: " + pw);

        model.addAttribute("id", id);
        model.addAttribute("pw", pw);
        return "dologin";
    }

    @GetMapping("/join")
    public String join() {
        return "join";
    }

    @PostMapping("/join")
    public String join(HttpServletRequest request, Model model) {
        String id = request.getParameter("id");
        String pw = request.getParameter("pw");
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String phone = request.getParameter("phone");
        String gender = request.getParameter("gender");

        String[] hobbys = request.getParameterValues("hobby");
        String hobby = Arrays.toString(hobbys);


        System.out.println(String.format("id: %s, pw: %s, name: %s, email: %s, phone, %s, gender, %s, hobby: %s", id, pw, name, email, phone, gender, hobby));

        model.addAttribute("id", id);
        model.addAttribute("pw", pw);
        model.addAttribute("name", name);
        model.addAttribute("email", email);
        model.addAttribute("phone", phone);
        model.addAttribute("gender", gender);
        model.addAttribute("hobby", hobby);
        

        return "dojoin";
    }
}