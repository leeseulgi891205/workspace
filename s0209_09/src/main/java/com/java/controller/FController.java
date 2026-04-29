package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.servlet.http.HttpServletRequest;

@Controller
public class FController {

    @GetMapping("/")
    public String main() {
        return "main";
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @PostMapping("/login")
    public String doLogin(HttpServletRequest request, Model model) {
        String id = request.getParameter("id");
        String pw = request.getParameter("pw");
        System.out.println("[login] id=" + id + ", pw=" + pw);
        model.addAttribute("id", id);
        return "main";
    }

}