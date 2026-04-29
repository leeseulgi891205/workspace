package j0116_01;

import java.util.Scanner;

public class c04 {

	public static void main(String[] args) {
		System.out.println(1.23456789);
		System.out.println(10/(double)3);
		// printf -> %
		// %d : 정수형
		System.out.printf("%010d,%.2f",123,10/(double)3);
		
		System.out.printf("d=%14.10f%n", 10/(double)3);
		
		// 출력
		System.out.printf("%n");
		// 입력 - System : console에서 입력을 받겠다.
		Scanner scanner = new Scanner(System.in);
		System.out.printf("숫자를 입력하세요.>>\n");
		int num = scanner.nextInt(); //정수형 입력
		System.out.println("입력한 숫자는 "+num+"입니다.");
		
		// input("숫자를입력하세요.") -> 파이썬
		
	}

}
