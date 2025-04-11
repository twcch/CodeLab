package com.example.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@EnableWebMvc
public class AppConfig {

    @Bean
    public String exampleBean() {
        return "This is an example bean";
    }

    // Additional bean definitions can be added here
}