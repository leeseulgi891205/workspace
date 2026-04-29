package com.java.www.main;

import org.springframework.stereotype.Service;

@Service // IOC 컨테이너에 여기 class 객체를 넣어줘
public class Tv extends Product {
	String name;
	int price;
}
