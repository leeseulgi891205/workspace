package j0116_01;

import java.util.Scanner;

public class C04 {

	public static void main(String[] args) {
		System.out.println(1.2345678);
		System.out.println((double)10 / 3 );  //10.0/3 = 3.33333
		
		// printf -> %
		// d-정수, f-실수
		System.out.printf("%010d, %.2f",123,  10/(double)3);
		
		// 출력
		System.out.println();
		
		
		// 입력 - System : console에서 입력을 받겠다.
		Scanner scanner = new Scanner(System.in);
		System.out.printf("숫자를 입력하세요.>> \n");
		int num = scanner.nextInt(); //정수형타입 값을 받음
		System.out.println("입력숫자 : "+num);
		
//		input("숫자를 입력하세요.")
		
		
		

	}

}
