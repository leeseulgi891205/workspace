package j0119_01;

import java.util.Scanner;

//내장객체는 import해야 사용가능 - System,Math

public class C0119_01 {

	public static void main(String[] args) {
		
	    char ch = 'A';
	    System.out.println(ch);
	    System.out.println((int) ch);
	    System.out.println(ch+1);  // byte,short,char -> + 연산을 하면 int타입
	    int ch2 = 65;
	    System.out.println((char)ch2);
	    
	    String str = "aaa";
//	    System.out.println(str+77-11); //에러 - 문자열+숫자 => 문자열 + 문자열 - 숫자(안됨)
	    System.out.println(77-11+str);
		
		
		
//		int True = 10;
////		int true; //예약어 안됨.
//		boolean a7 = true;
//		boolean b = false;
//		byte c = 1;  //256개 -128~127
//		short d = 1;  //
//		int e = 1;
//		long f = 10000000000L;
//		float g = 1.0F;
//		double h$_a = 1.0d;
//		char cc = 'a';  // 문자1개만 가능, 2개 안됨.
//		char cc2 = ' ';
////		char cc3 = ''; // 아무것도 넣지 않는 것은 안됨.
//		
//		String str = new String("aaa");
//		System.out.println(str);
//		
//		String str2 = "aaa"; //String 객체만 new를 사용하지 않아도 됨.
//		System.out.println(str2);
//		
		
		
		
//		int a = 2_147_483_647;
//		System.out.println(a+10);
//		
//		int b = 10;
//		System.out.println(b+1);
		
		
		// 함수 -> 메소드
		// 함수,객체 차이점 -> 이름():함수, 클래스:첫글자가 대문자
//		System.out.println("출력입니다.");
//		// 입력부분 - 객체선언
//		Scanner scanner = new Scanner(System.in);
//		System.out.println("숫자를 입력하세요.");
//		int a = scanner.nextInt();
//		//input("숫자를 입력하세요.") - 파이썬
//		
//		System.out.println("입력된 숫자 : "+a);
		
		
		

	}

}
