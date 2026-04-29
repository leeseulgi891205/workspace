package com.java.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.http.HttpMethod;

@Configuration
public class SecurityConfig {

    @Bean
    public UserDetailsService users() {
        InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser(User.withDefaultPasswordEncoder().username("user").password("password").roles("USER").build());
        return manager;
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                // Allow public GET access to board list and detail
                .requestMatchers(HttpMethod.GET, "/board", "/board/*").permitAll()
                // Require authentication for board modifications (POST/PUT/DELETE under /board/**)
                .requestMatchers(HttpMethod.POST, "/board/**").authenticated()
                .requestMatchers("/auth/**").permitAll()
                .requestMatchers("/", "/main", "/notice", "/guide", "/report", "/css/**", "/js/**", "/images/**").permitAll()
                .anyRequest().permitAll()
            )
            .formLogin(form -> form
                .loginPage("/auth/login")
                .defaultSuccessUrl("/board", true)
                .permitAll()
            )
            .logout(logout -> logout.permitAll())
            .csrf(csrf -> csrf.disable()); // updated for Spring Security 6
        return http.build();
    }
}