package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {
    @GetMapping("hello")
    public String Hello(Model model) {                                  // mvc패턴의 model
        model.addAttribute("data", "hello!!");
        return "hello";                                                 // thymeleaf 엔진이 처리한 resources/templates/hello.html을 렌더링해라
    }
}
