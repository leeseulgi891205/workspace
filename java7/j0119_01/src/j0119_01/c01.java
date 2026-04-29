package j0119_01;

import java.util.Scanner;

public class c01 {



	public static void main(String[] args) {
		
		char ch = 'A';
		System.out.println(ch); // 65
		System.out.println((int)ch); //- char -> int 형변환
		System.out.println(ch+1); // byte, short, int, long, float, double 형변환 > 연산을 하면 int
		int ch2 = 65;
		System.out.println((char)ch2); // int -> char 형변환
		
		String str = "aaa";
		System.out.println(str+77); // 문자열 + 숫자 = 문자열
		System.out.println(77-11+str); // 숫자 + 문자열 = 문자열
		System.out.println(str+(77-11)); // 문자열 + 숫자 = 문자열
		
		// int -> char 형변환 불가
		// char -> int 형변환 가능
		// flat  -> int 형변환 불가
		// int -> float 형변환 가능
		
		
		//byte<short<int<long<float<double<Strung
		//문자열 +만 가능
		//숫자 +,-*,/,% 가능
		
		
		
		
//		int True = 10;
//		// int true; // 예약어 사용 불가
//		boolean a = true; // 논리형 변수 선언
//		boolean b = false;
//		byte c = 1; // 256개 - 128 ~ 127
//		short d = 1;
//		int e = 1;
//		long f = 1000000000L; // 8byte
//		float g = 1.0F; // 4byte - 소수점 7자리 - F,f 붙여야함
//		double h = 1.0; // 8byte - 소수점 15자리 
//		char cc = 'A'; // 문자형 변수 선언 - 홑따옴표 2개 불가
//		char cc2 = ' '; // 공백 문자
//		// char cc3 =''; // 아무것도 넣지 않는 것은 안됨. 	
//		
//		String str = new String("aaa"); // 문자열 변수 선언 - 쌍따옴표
//		System.out.println(str);
//		
//		String str2 = "aaa"; // 스트링 객체만 뉴를 사용하지 않아도 됨
//		System.out.println(str2);
//		
//		// 입력부분 - 객체선언
//		// 고급언어 
		Scanner Scanner = new Scanner(System.in);
//		
//		int num1 = 2147483647; // 4byte
//		System.out.println(num1+10); // 오버플로우 발생
//		
//		int num2 = 10;
//		System.out.println(num2+1);
		
//		// 함수 -> 메서드
//		// 함수 객체 차이점 -> 이름: 함수 객체: 메서드 클래스: 첫글자가 대문자
//		System.out.println("출력입니다.");
//
//
//		
//		// 입력부분 - 객체선언
//		
//		System.out.print("숫자를 입력하세요: ");
//		int a = Scanner.nextInt(); // 정수형 입력
//		
//		
//		System.out.println("입력한 숫자는: " + a);
//		Scanner.close(); // Scanner 객체 닫기
		
	}

}
