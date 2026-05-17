package com.docker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@SpringBootApplication
@RestController
public class App {

    private List<Map<String, Object>> tasks = new ArrayList<>();

    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "healthy", "runtime", "Java Spring Boot");
    }

    @GetMapping("/tasks")
    public List<Map<String, Object>> getTasks() {
        return tasks;
    }

    @PostMapping("/tasks")
    public Map<String, String> addTask(@RequestBody Map<String, String> body) {
        Map<String, Object> task = new HashMap<>();
        task.put("id", tasks.size() + 1);
        task.put("task", body.get("task"));
        tasks.add(task);
        return Map.of("message", "Task '" + body.get("task") + "' added!");
    }
}
