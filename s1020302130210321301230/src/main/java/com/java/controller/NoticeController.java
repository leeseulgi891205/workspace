package com.java.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicLong;

@Controller
@RequestMapping
public class NoticeController {

    private final List<Notice> notices = Collections.synchronizedList(new ArrayList<>());
    private final AtomicLong idCounter = new AtomicLong(1);

    @GetMapping("/notice")
    public String notice(Model model) {
        model.addAttribute("notices", notices);
        return "notice";
    }

    @GetMapping("/notice/{id}")
    public String detail(@PathVariable long id, Model model) {
        Optional<Notice> n = notices.stream().filter(x -> x.getId() == id).findFirst();
        if (n.isEmpty()) return "redirect:/notice";
        model.addAttribute("notice", n.get());
        return "notice-detail";
    }

    @GetMapping("/notice/{id}/edit")
    public String editForm(@PathVariable long id, Model model) {
        Optional<Notice> n = notices.stream().filter(x -> x.getId() == id).findFirst();
        if (n.isEmpty()) return "redirect:/notice";
        model.addAttribute("notice", n.get());
        return "notice-edit";
    }

    @PostMapping("/notice/post")
    public String postNotice(@RequestParam String title, @RequestParam String content) {
        Notice n = new Notice(idCounter.getAndIncrement(), title, content, LocalDateTime.now());
        notices.add(0, n);
        return "redirect:/notice";
    }

    @PostMapping("/notice/{id}/edit")
    public String editNotice(@PathVariable long id, @RequestParam String title, @RequestParam String content) {
        synchronized (notices) {
            for (Notice no : notices) {
                if (no.getId() == id) {
                    no.setTitle(title);
                    no.setContent(content);
                    break;
                }
            }
        }
        return "redirect:/notice/" + id;
    }

    @PostMapping("/notice/{id}/delete")
    public String deleteNotice(@PathVariable long id) {
        synchronized (notices) {
            notices.removeIf(n -> n.getId() == id);
        }
        return "redirect:/notice";
    }

    public static class Notice {
        private long id;
        private String title;
        private String content;
        private LocalDateTime createdAt;

        public Notice(long id, String title, String content, LocalDateTime createdAt) {
            this.id = id;
            this.title = title;
            this.content = content;
            this.createdAt = createdAt;
        }

        public long getId() { return id; }
        public String getTitle() { return title; }
        public String getContent() { return content; }
        public LocalDateTime getCreatedAt() { return createdAt; }

        public void setTitle(String title) { this.title = title; }
        public void setContent(String content) { this.content = content; }
    }
}