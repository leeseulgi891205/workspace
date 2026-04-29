package com.java;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.mybatis.spring.annotation.MapperScan;

@MapperScan("com.javaDao")
@SpringBootApplication
public class S021101Application {

	public static void main(String[] args) {
		SpringApplication.run(S021101Application.class, args);
	}

}
