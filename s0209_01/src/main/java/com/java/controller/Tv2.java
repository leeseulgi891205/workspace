package com.java.controller;

import org.springframework.stereotype.Service;

@Service
public class Tv2 implements Product {
	public String getName() {
		String name = "Samsung TV 버전 2";
		return name;
	}
}
