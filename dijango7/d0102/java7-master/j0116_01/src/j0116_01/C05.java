package j0116_01;

import java.util.Scanner;

public class C05 {

	public static void main(String[] args) {
		// String 문자열타입 : next()-사이띄움X,enter키 입력X , nextLine()-사이띄움,enter키
		// 정수타입  : nextInt(), nextLong() 
		// 실수타입 : nextFloat(), nextDouble()
		Scanner scanner = new Scanner(System.in);
		// 이름,국어,영어 입력받아서, 출력하시오.
		System.out.println("이름을 입력하세요. >> ");
		String name = scanner.next();
		System.out.println("국어점수를 입력하세요.>> ");
		int kor = scanner.nextInt();
		System.out.println("영어점수를 입력하세요.>> ");
		int eng = scanner.nextInt();
		System.out.printf("이름:%s,국어:%d,영어:%d",name,kor,eng);
		
		
		
//		System.out.println("이름을 입력하세요. >> ");
//		String name = scanner.next();
//		System.out.println("국어점수를 입력하세요.>> ");
//		int kor = scanner.nextInt();
//		
//		System.out.println("이름 : "+name+" 국어점수 : "+kor);
		
		
//		System.out.println("이름을 입력하세요.>> ");
//		String name = scanner.nextLine();
//		System.out.println("아이디를 입력하세요.>> ");
//		String id = scanner.nextLine();
//		System.out.println("이름 : "+name);
//		System.out.println("아이디 : "+id);
		

	}

}
