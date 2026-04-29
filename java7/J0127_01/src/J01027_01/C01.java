package J01027_01;

import java.util.*; // Date, Scanner 클래스를 사용하기 위해서

import member.Login;

public class C01 {
	C01(){}

	public static void main(String[] args) {
		
		Deck d = new Deck(); // 카드한 묶음
//		d.pick(39);
//		d.pick(50);
//		d.pick(2);
//		d.pick(1);
//		d.pick(0);
//		d.c[1].number = 13;
		
		d.cardAllPrint();// 카드 전체 출력 // 섞기 전
		d.shuffle();
		System.out.println("----------");
		d.cardAllPrint();// 섞은 후 카드 전체 출력
		
		Login l = new Login();
		System.out.println("id : " + l.id);
		System.out.println("pw : " + l.pw);
		
		System.out.println(d.c[0].number);

		


		
		
		
		
		
		
//		Circle c1 = new Circle();
//		System.out.println("c1.color");

	}

}