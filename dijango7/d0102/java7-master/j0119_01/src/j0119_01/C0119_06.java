package j0119_01;

import java.util.Scanner;

public class C0119_06 {

	public static void main(String[] args) {
		
		int count = 0;
		String num = "9789057899979971234567";
		
		// indexOf() 메소드,for문을 이용해서 
		// 7이 있는지 위치와 7이 총 몇개가 있는지 출력하시오.
		
		
		
		
		
		
		
//		System.out.println(num.indexOf("7",15));
		
		
//		if(num.indexOf("7")==-1) {
//			System.out.println("해당문자가 없습니다.");
//		}else {
//			System.out.println("문자위치 : "+num.indexOf("7"));
//		}
		
		
		
//		String num = "1234567";
//		// charAt() : 문자열에서 해당위치값을 문자로 변환
//		
//		//indexOf() 메소드 : 해당문자열이 있는경우 위치값을 알려줌, 없으면 -1리턴
////		System.out.println(num.indexOf("8"));
//		
//		if(num.indexOf("7")==-1) {
//			System.out.println("해당문자가 없습니다.");
//		}else {
//			System.out.println("문자위치 : "+num.indexOf("8"));
//		}
		
		
		// contains : 해당문자열이 있는지 확인하는 메소드
//		if(num.contains("8")) {
//			System.out.println("7이 존재합니다.");
//		}else {
//			System.out.println("7이 존재하지 않습니다.");
//		}
		
		
		
		
		
		
//		Scanner scanner = new Scanner(System.in);
//		
//		// 랜덤숫자(0-9까지숫자) 1개를 생성해서
//		// 입력받은 숫자 7개 중에 랜덤숫자랑 똑같은 숫자가 몇개인지 출력하시오.
//		int rnum = (int)(Math.random()*10); //8
//		int r = (char)(rnum+'0');
//		
//		// int 숫자타입을 char숫자타입으로 변경방법
//		// (char)(1+'0') = 1+48 = 49 : 문자(1)
//		// char숫자타입을 int타입으로 변경방법
//		// '7'-'0' = int타입 7	
//		
//		char ch = (char)(rnum+'0');
//		int count = 0;
//		System.out.println("숫자를 입력하세요.>> ");
//		String input = scanner.next();
//		
//		for(int i=0;i<input.length();i++) {
//			if(input.charAt(i)==ch) count++;
//		}
//		
//		System.out.println("랜덤숫자 : "+ch);
//		System.out.println("입력숫자 : "+input);
//		System.out.println("결과 : "+count);
		
		
		
		// 숫자 5개를 입력받아, 7이 몇개 입력되었는지 출력하시오.
		// 12347
//		int count = 0;
//		System.out.println("숫자를 입력하세요.>> ");
//		String input = scanner.next();
//		
//		for(int i=0;i<input.length();i++) {
//			if(input.charAt(i)=='7') count++;
//		}
//		
//		System.out.println(input.length());
//		System.out.println("입력숫자 : "+input);
//		System.out.println("결과 : "+count);
		
		
//		0-9랜덤숫자 5개를 생성해서 -> 14567 -> 7이 몇개 있는지 출력하시오.
//		int count = 0;
//		String random_num = "";
//		
//		for(int i=0;i<5;i++) {
//			int rnum = (int)(Math.random()*10); 
//			random_num += rnum;
//			if (rnum==7) count++;
//			
//		}
		
//		System.out.println("랜덤숫자 : "+random_num);
//		System.out.println("결과값 : "+count);
		
		
//		int sum = 0;
//		int i=0;
//		for(i=1;i<=10;i++) {
//			sum += i;
//			System.out.println(i+","+sum);
//		}
		
		
		
		// 1~100까지의 홀수의 합이 100을 넘는 시점의 i의 값과 sum을 출력하시오.
//		for(int i=1;i<=100;i++) {
//			if (i%2==1) {
//				sum += i;
//				if(sum>100) {
//					System.out.println(i+","+sum);
//					break;
//				}
//			}
//		}
		
		
		
//		int sum = 0;
//		
//		for(int i=1;i<=10;i++) {
//			sum += i;
//			System.out.println(i+","+sum);
//		}
		
		
		
//		System.out.println(1);
//		System.out.println(2);
//		System.out.println(3);
//		
//		for(int i=1;i<=5;i++) {
//			System.out.println(i);
//		}
		
		
		
		
		//0~9까지 랜덤숫자를 5개를 출력하시오. 15467
//		System.out.println((int)(Math.random()*10));
		
		
		
//		int r_num = (int)(Math.random()*10);
//		int r_num2 = (int)(Math.random()*10);
//		int r_num3 = (int)(Math.random()*10);
//		int r_num4 = (int)(Math.random()*10);
//		int r_num5 = (int)(Math.random()*10);
//		System.out.printf("%d%d%d%d%d\n",r_num,r_num2,r_num3,r_num4,r_num5);
		
		
		// 랜덤숫자 확인
		//0~9
//		int r_num = (int)(Math.random()*10);
//		//0~99
//		int r_num2 = (int)(Math.random()*100);
//		//0~49
//		int r_num3 = (int)(Math.random()*50);
		
		
//		//1~45까지 랜덤숫자를 출력하시오.
//		int random_num = (int)(Math.random()*45)+1;
//		//1~100까지 랜덤숫자를 출력하시오.
//		int random_num2 = (int)(Math.random()*100)+1;
//		System.out.println(random_num);

	}

}
