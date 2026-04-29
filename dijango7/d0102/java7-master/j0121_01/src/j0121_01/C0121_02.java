package j0121_01;

import java.util.Scanner;

public class C0121_02 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		//퀴즈 - 1조123456
		// 6 - 500원
		// 56 - 1000원
		// 456 - 10000원
		// 3456 - 10만원
		// 23456 - 100만원
		// 123456 - 1000만원
		
		// 6자리를 랜덤으로 복권번호 생성
		// 0 - 999999 랜덤번호 생성해서 출력하시오.
		int random = (int)(Math.random()*1000000);
		String lotto = String.format("%06d", random);
		System.out.println(lotto);
		
		// 프로그램을 구현하시오.
		// 입력번호(000005) 와 끝번호가 맞는지 확인해서 맞춤,틀림 출력하시오.
		System.out.println("6자리 숫자를 입력하세요.>> ");
		String input = scanner.next();
		
		if(input.charAt(5)==lotto.charAt(5)) 
			System.out.println("500원 당첨!");
		else 
			System.out.println("틀림");
		
		
//		if(input.charAt(5)==lotto.charAt(5)) 
//			if(input.charAt(4)==lotto.charAt(4)) 
//				if(input.charAt(3)==lotto.charAt(3))
//					if(input.charAt(2)==lotto.charAt(2))
//						if(input.charAt(1)==lotto.charAt(1))
//							if(input.charAt(0)==lotto.charAt(0))
//								System.out.println("1000만원 당첨!");
//							else
//								System.out.println("100만원 당첨!");
//						else
//							System.out.println("10만원 당첨!");
//					else
//						System.out.println("10000원 당첨!");
//				else
//					System.out.println("1000원 당첨!");
//			else 
//				System.out.println("500원 당첨!");
//		else 
//			System.out.println("틀림");
		
		
		
		
		
		
		
//		Scanner scanner = new Scanner(System.in);
//		String[] binary = {
//			"0000","0001","0010","0011",	// 0,1,2,3
//			"0100","0101","0110","0111",	// 4,5,6,7
//			"1000","1001"	                // 8,9
//		};
//		
//		// 1987 -> 0001 1001 1000 0111
//		// 0752 -> String타입으로 입력받음.
//		// 숫자 1개를 입력받아, 2진수를 출력하시오.
//		
//		System.out.println("숫자를 입력하세요.>> ");
////		int input = scanner.nextInt();
////		System.out.println(binary[input]);
//		String input = scanner.next();
//		System.out.println(binary[Integer.parseInt(input)]);
////		System.out.println(binary[input.charAt(0)-'0']);
		
		
		
		
		
//		System.out.println("숫자를 입력하세요.>> ");
//		String input = scanner.next();
		
//		// 1234
//		for(int i=0;i<input.length();i++) {
//			System.out.println(binary[input.charAt(i)-'0']);
//			// binary['1'-'0'];
//		}
		
		
		
		
//		// 숫자타입 -> 문자열타입
//		System.out.println(""+7+7.7); //문자열타입으로 변경
//		
//		// 문자열타입 -> int타입,double타입
//		int a = Integer.parseInt("77");
//		double b = Double.parseDouble("77.7");
//		
//		// 문자(char)숫자타입 -> int타입
//		System.out.println('9'-'0'); // int 9
//		
//		// int타입 -> char타입으로 변경
//		System.out.println((char)(9+'0')); // char타입 9
		
		
		
		

	}

}
