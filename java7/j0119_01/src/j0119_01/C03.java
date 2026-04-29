package j0119_01;

import java.util.Scanner;

public class C03 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// 숫자 5개를 연속으로 입력받아 합계를 출력하시오. 12345 = 15
		System.out.println("숫자 5개를 연속으로 입력하세요.(12345)>>");
		String num = scanner.next();
		char ch1 = num.charAt(0);
		char ch2 = num.charAt(1);
		char ch3 = num.charAt(2);
		char ch4 = num.charAt(3);
		char ch5 = num.charAt(4);
		int sum = (ch1-'0')+(ch2-'0')+(ch3-'0')+(ch4-'0')+(ch5-'0');
		System.out.println("결과 :"+sum);
		
		
		
		
		
		
		
		
		// 1+3 = 4
		// 1. 숫자 2개를 입력받는다.
		// 2. 두 숫자의 합을 구한다.
		// 3. 결과를 출력한다.
		
//		System.out.println("숫자를 한번에 입력하세요.(13)>>");
//		String num = scanner.next();
//		char ch = num.charAt(0);
//		char ch2 = num.charAt(1);
//		System.out.println(ch+","+ch2);
//		System.out.println("결과값 :");
//		// 결과 값 9가 출력되도록 출력하시오.
//		System.out.println(ch+","+ch2 );
//		System.out.println("결과값: ");
		
		
		
//		System.out.println("숫자를 입력하세요.>>");
//		int num = scanner.nextInt();
//		System.out.println("숫자2를 입력하세요.>>");
//		int num2 = scanner.nextInt();
//		System.out.printf("숫자1:%d, 숫자2:%d \n",num, num2);
		
		
		
//		int i = 'b'-'a';
//		System.out.println(i); // 1
//		
//		int j = '2'-'0';
//		System.out.println(j); // 2
//		
//		int k = '5'-'0';
//		System.out.println(k); // 5
//		
//		char ch = '5';
//		int num = ch-48;
//		System.out.println(num);
		
		
		
		
		
//		char ch1 = 'A'; // 97 
//		System.out.println(ch1); // A
//		char ch2 = ch1+1; // 오류발생
//		int ch2 = ch1+1; // 형변환 발생
//		System.out.println(ch2);
//		System.out.println((char)ch2); // B
//		
//		ch1++; // ch1 = ch1 +1;
//		
//		char ch3 = ch1; // char특징 : ++,-- 실행가능
//		System.out.println(ch3); // B
		
		
		
		
		
//		int a = 1_000_000;
//		int b = 2_000_000;
//		long c = (long)a * (long)b; // 형변환을 해줘야함 안그러면 오버플로우 발생
//		System.out.println(c);
		
		
		
//		//단항연산자 - 부호연산자 - ++, --, +, -
//		int a = -10;
//		System.out.println(a);
//		int b = 10;
//		System.out.println(b);
//		
//		// 단항연산자 - 증감연산자
//		// a++; // a =a +1; , a= a+1
//		// b--; // b =b -1; , b= b-1
//		
//		
//		// 논리연산자 - &&(AND), ||(OR), !(NOT)
//		
//		
//		// 산술연산자 - + - * / %
//		System.out.println(10+3);
//		System.out.println(10-3);
//		System.out.println(10*3);
//		System.out.println(10/3);
//		System.out.println(10%3); // 나머지 연산
//		
//		// 비교연산자 - > < >= <= == !=
//		
//		// 삼항연산자 - (조건) ? 참 : 거짓
//		String str = (a>b) ? "맞습니다." : "틀렸습니다.";
//		System.out.println(str);
//		
//		// 이항연산자 - + - * / % > < >= <= == != && ||
//		// 피연산자 -

	}

}
