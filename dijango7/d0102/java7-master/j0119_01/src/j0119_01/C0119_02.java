package j0119_01;

import java.util.Scanner;

public class C0119_02 {

	public static void main(String[] args) {
		// 변수 - boolean,char,(정수:byte,short,int,long),(실수:float,double),String
		// Scanner -> (String) next(),nextLine()
		// nextBoolean(),nextInt(),nextLong(),nextDouble(),nextFloat()
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("이름을 입력하세요.>> ");
		String name = scanner.next(); //사이띄움 안됨, enter키 입력없음.
		System.out.println("이름 : "+name);
		
//		System.out.println("안녕"+5.8);
//		System.out.print(3+5+"방가"+4+2+"\n");
//		System.out.printf("%s:%d","홍길동",15);
		
//		이름과 실수를 입력해서(실수소수점 3자리까지 입력) 소수점 첫째자리까지 출력하시오.
//		Scanner scanner = new Scanner(System.in);
//		System.out.println("이름을 입력하세요.>> ");
//		String name = scanner.next();
//		System.out.println("실수를 입력하세요.>> ");
//		double num = scanner.nextDouble();
//		
//		// 출력하시오. 소수점 3자리, 1자리까지 출력하시오.
//		// printf() 함수를 사용해서 출력하시오.
//		System.out.printf("이름:%s, 숫자:%.1f",name,num);
		
		
		
		
		
		
		
//		int a = 10;
//		int b = 3;
//		System.out.println(a/(double)b); // 3
//		// 소수점자리수 출력가능, 공백크기 지정가능, 공백 0표시 가능
//		System.out.printf("%.2f",(a/(double)b));

	}

}
