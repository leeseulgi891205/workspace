package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Controller
@RequestMapping
public class InfoController {

    private final List<Post> posts = Collections.synchronizedList(new ArrayList<>());

    @GetMapping("/guide")
    public String guide() {
        return "guide";
    }

    @GetMapping("/board")
    public String board(Model model) {
        model.addAttribute("posts", posts);
        return "board";
    }

    @PostMapping("/board/post")
    public String postToBoard(@RequestParam String title, @RequestParam String content) {
        Post p = new Post(title, content, LocalDateTime.now());
        posts.add(0, p); // newest first
        return "redirect:/board";
    }

    @GetMapping("/report")
    public String report() {
        return "report";
    }

    public static class Post {
        private String title;
        private String content;
        private LocalDateTime createdAt;

        public Post(String title, String content, LocalDateTime createdAt) {
            this.title = title;
            this.content = content;
            this.createdAt = createdAt;
        }

        public String getTitle() { return title; }
        public String getContent() { return content; }
        public LocalDateTime getCreatedAt() { return createdAt; }
    }
}