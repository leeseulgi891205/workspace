package j0120_01;

import java.util.Arrays;
import java.util.Scanner;

public class C0120_03 {
	
//	static int aa; //클래스내 변수 초기화 됨.

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		int[] num = new int[10];
		for(int i=0;i<num.length;i++) {
			num[i] = i+1;
		}
		
		System.out.println("순차번호 : "+Arrays.toString(num));
		
		// 랜덤숫자 섞기
		for(int i=0;i<300;i++) {
			int no = (int)(Math.random()*10); //0-9
			int temp = num[0];
			num[0] = num[no];
			num[no] = temp;
		}
		
		System.out.println("랜덤번호 : "+Arrays.toString(num));
		
		
		
		
		
		
		
//		int[] num = new int[3];
//		int a = 0;
//		int a2 = 0;
//		int a3 = 0;
//		// 1~3까지 랜덤숫자를 변수에 각각 다른 숫자를 입력해서 출력하시오.
//		// 배열을 사용해서 
//		// 각각 다른 랜덤숫자를 입력해서 출력하시오.
//		num[0] = (int)(Math.random()*3)+1;
//		int i = 1;
//		loop:while(true) {
//			num[i] = (int)(Math.random()*3)+1;
//			if(num[i]!=num[i-1]) {
//				i++;
//				while(true) {
//					num[i] = (int)(Math.random()*3)+1;
//					if(num[i]!=num[i-1] && num[i]!=num[i-2] ) {
//						break loop;
//					}
//				}
//			}//if
//		}
//		
//		System.out.println("[ 랜덤번호 ]");
//		for(i=0;i<num.length;i++) {
//			System.out.print(num[i]+" ");
//		}
		
		
		
		
		
//		while(true) {
//			a2 = (int)(Math.random()*3)+1;
//			a3 = (int)(Math.random()*3)+1;
//			if(a!=a2 && a!=a3 && a2!=a3) {
//				break;
//			}
//		}
		
		
		
		
//		String[] name = new String[3];
//		int[] kor = new int[3];
//		
//		// 이름,국어 점수를 입력받아, 3명 모두 출력하시오.
//		for(int i=0;i<name.length;i++) {
//			System.out.println("이름을 입력하세요.>> ");
//			name[i] = scanner.next();
//			System.out.println("국어점수를 입력하세요.>> ");
//			kor[i] = scanner.nextInt();
//		}
//		
//		for(int i=0;i<name.length;i++) {
//			System.out.printf("%s\t%d\n",name[i],kor[i]);
//		}
		
		
		
		
		
//		int[] a = new int[3];
//		int[] input = new int[3];
//		// 1-10번 랜덤숫자 5개, 입력받아 5개 생성해서 배열에 넣고 출력하시오.
//		for(int i=0;i<a.length;i++) {
//			a[i] = (int)(Math.random()*10)+1;
//			System.out.println("숫자를 입력하세요.>> ");
//			input[i] = scanner.nextInt();
//		}
//		
//		for(int i=0;i<a.length;i++) {
//			System.out.printf("%d\t",a[i]);
//		}
//		System.out.println();
//		for(int i=0;i<input.length;i++) {
//			System.out.printf("%d\t",input[i]);
//		}
//		System.out.println();
		
		
		
		
		
		
		//입력을 3개 받아서 출력하시오.
//		int[] a = new int[3];
//		a[0] = 1;
//		a[1] = 1.1;
//		a[2] = "홍길동";
		
//		for(int i=0;i<3;i++) {
//			System.out.println("숫자를 입력하세요.>> ");
//			a[i] = scanner.nextInt();
//		}
//		
//		for(int i=0;i<3;i++) {
//			System.out.print(a[i]+" ");
//		}
		
		
//		System.out.println("숫자를 입력하세요.>>");
//		int a = scanner.nextInt();
//		System.out.println("숫자를 입력하세요.>>");
//		int a2 = scanner.nextInt();
//		System.out.println("숫자를 입력하세요.>>");
//		int a3 = scanner.nextInt();
//		
//		System.out.printf("%d,%d,%d \n",a,a2,a3);
		
		
		
		
//		int[] score = new int[5];
//		for(int i=0;i<5;i++) {
//			score[i] = i+1;
////			System.out.println(score[i]);
//		}
//		
//		for(int i=0;i<5;i++) {
//			System.out.println(score[i]);
//		}
		
		
		
		
		
		// 배열에 값을 입력하는 방법
//		int[] score = new int[5];
//		score[0] = 1;
//		score[1] = 2;
//		score[2] = 3;
//		score[3] = 4;
//		score[4] = 5;
//		
//		int[] num = {1,2,3,4,5}; //가장많이 사용
//		int[] num2 = new int[] {1,2,3,4,5};
		
		
		
		
		
		// 메소드내에 변수들은 초기화를 해야 실행이 가능함.
//		int a; // 메소드내 자동초기화 안됨.
////		System.out.println(a);
//		System.out.println(aa);
//
//		int[] score = new int[5]; // 배열은 자동초기화가 됨.
//		System.out.println(score[0]);
//		System.out.println(score[1]);
//		System.out.println(score[2]);
//		System.out.println(score[3]);
//		System.out.println(score[4]);
//		System.out.println(score);
		
	}

}
