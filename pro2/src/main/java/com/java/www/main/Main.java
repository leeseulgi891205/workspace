package com.java.www.main;

public class Main {

	public static void main(String[] args) {
		//1. 각각의 클래스를 객체선언해서 사용
//		Tv tv = new Tv();
//		Tv2 tv2 = new Tv2();
//		tv2.name = "Smart TV";
//		System.out.println(tv2.name);
		
		//2. 부모의 참조변수로 객체선언해서 사용
		//Product product = new Tv();
//		Product product = new Tv2();
//		product.name = "Another TV";
//		System.out.println(product.name);
		
		//3. 스프링사용
		//@AutoWired
		Product product;
//		Product.name = "Spring TV";
//		System.out.println(Product.name);
	}

}
