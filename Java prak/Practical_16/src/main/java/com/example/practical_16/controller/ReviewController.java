package com.example.practical_16.controller;

import com.example.practical_16.model.Review;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;
import java.util.List;

@Controller
public class ReviewController {

    private List<Review> reviews = new ArrayList<>();

    @GetMapping("/reviews")
    public String showForm(Model model) {
        model.addAttribute("reviews", reviews);
        return "reviews"; // Имя шаблона (например, home.html в папке templates)
    }

    @PostMapping("/reviews")
    public String handleReviewSubmission(@RequestParam String reviewContent, Model model) {
        Review review = new Review(reviewContent);
        reviews.add(review);
        model.addAttribute("reviews", reviews);
        return "reviews";
    }
}
