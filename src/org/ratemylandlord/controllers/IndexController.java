package org.ratemylandlord.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * Created by saurabh on 2/11/17.
 */

@Controller
public class IndexController {
    @GetMapping("/")
    public String index(Model m) {
        return "index";
    }
}