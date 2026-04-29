package J0120_01;

import java.util.Arrays;
import java.util.Scanner;

public class C03 {
	
	static int aa; //클래스내 변수 초기화 됨.

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int[] num = new int[10];
		for(int i=0;i<num.length;i++) {
			num[i] = i+1;
		}
		System.out.println("순차번호 :"+Arrays.toString(num));
		
		// 랜덤숫자 섞기
		for(int i=0;i<300;i++) {
			int no = (int)(Math.random()*10); //0-9
			int temp = num[0];
			num[0] = num[no];
			num[no] = temp;
		}
		System.out.println("랜덤번호 :"+Arrays.toString(num));
		
		
		
		
		
		
//		int[] num = new int[3];
//		int a = 0;
//		int a2 = 0;
//		int a3 = 0;
//		// 1~3까지의 랜덤숫자를 변수에 각각 다른 숫자를 입력해서 출력하시오.
//		num[0] = (int)(Math.random()*3)+1;
//		// 배열을 사용해서 각각 다른 랜덤숫자를 입력해서 출력하시오.
//		int i = 1;
//		loop:while(true) {
//			num[i] = (int)(Math.random()*3)+1;
//			if(num[i]!=num[0]) {
//				if(i==2) {
//					break loop;
//				}
//				i++;
//				while(true) {
//					num[i] = (int)(Math.random()*3)+1;
//					if(num[i]!=num[i-1]&&num[i]!=num[i-2]) {
//						break;
//					}
//				}
//				break loop;
//			}
//		}
//		System.out.println("랜덤숫자 3개 출력");
//		for(int j=0;j<3;j++){
//			System.out.printf("num[%d]:%d\n",j,num[j]);
//		}

		
		
		
//		while(true) {
//			a2=(int)(Math.random()*3)+1;
//			if(a!=a2)break;
//		}
//		while(true){
//			a3 = (int)(Math.random()*3)+1;
//			if(a!=a3&&a2!=a3) break;
//		}
//		System.out.printf("a:%d,a2:%d,a3:%d\n",a,a2,a3);
		
		
		
		
		
		
		
		
		
		
		
		
//		String[] name = new String[3];
//		int[] kor = new int[3];
//		
//		// 이름,국어 점수를 입력받아서, 마지막에 3명 모두 출력하시오.
//		for(int i=0;i<3;i++) {
//			System.out.print("이름을 입력해주세요.>>");
//			name[i] = scanner.next();
//			System.out.print("국어점수를 입력해주세요.>>");
//			kor[i] = scanner.nextInt();
//		}
//		for(int i=0;i<3;i++) {
//			System.out.printf("이름:%s, 국어점수:%d \n",name[i],kor[i]);
//		}
		
		
		
		
		
		
		

//		int[] a = new int[5];
//		for(int i=0;i<5;i++) {
//			System.out.print("숫자를 입력하세요.>>");
//			a[i] = scanner.nextInt();
//		}
//		System.out.println("입력한 숫자 5개는 다음과 같습니다.");
//		for(int i=0;i<5;i++) {
//			System.out.printf("입력한 숫자 %d : %d \n",i+1,a[i]);
//		}
//		
//		// 랜덤숫자 10개를 생성해서 배열에 넣고 출력하시오.
//		int[] b = new int[5];
//		for(int i=0;i<5;i++) {
//			b[i] = (int)(Math.random()*100)+1;
//		}
//		for(int i=0;i<10;i++) {
//			System.out.printf("랜덤:[%d]=%d\n",i,b[i]);
//		}
//		
		
		
		
		
		
		
		
		
//		// 입력을 3개를 받아서 출력하시오.
//		int[] a = new int[3];
//		a[0] = 1;
//		a[1] = 2;
//		a[2] = "홍길동".length();
//		
//		System.out.printf("입력한 숫자는 %d, %d, %d 입니다.\n",a[0],a[1],a[2]);
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
//		for(int i=0;i<3;i++) {
//			System.out.print("숫자를 입력하세요.>>");
//			a[i] = scanner.nextInt();
//			
//		}
//		
//		for(int i=0;i<3;i++) {
//			System.out.printf("입력한 숫자는 %d 입니다.\n",a[i]);
//		}
		
		
		
		
		
		
		
		
//		System.out.print("숫자를 입력하세요.>>");
//		int a = scanner.nextInt();
//		System.out.print("숫자을 입력하세요.>>");
//		String a2 = scanner.next();
//		System.out.print("숫자를 입력하세요.>>");
//		String a3 = scanner.next();
//		
//		System.out.printf("입력한 숫자는 %d, %s, %s 입니다.\n",a,a2,a3);
		
		
		
		
//		int[] score = new int[5];
//		for(int i=0;i<5;i++) {
//			score[i] = i+1;
////			System.out.println(score[i]);
//		}
//		
//		for(int i=0;i<5;i++) {
//			System.out.println(score[i]);
//		}
//		
		
		
		
//		// 배열에 값을 입력하는 방법
//		int[] score = new int[5]; // 배열은 자동 초기화도 됨.
//		score[0] = 1;
//		score[1] = 2;
//		score[2] = 3;
//		score[3] = 4;
//		score[4] = 5;
//		
//		int[] num = {1,2,3,4,5}; // 배열선언과 동시에 값 입력
//		int[] num2 = new int[] {1,2,3,4,5}; // 배열선언과 동시에 값 입력
		
		
		
		
		
//		Scanner scanner = new Scanner(System.in);
//		// 메소드내에 변수들은 초기화를 해야 실행이 가능함.
//		int a; // 메소드내 자동초기화 안됨.
////		System.out.print(a);
//		System.out.print(aa);
//		
//		
//		int[] score = new int[5]; // 배열은 자동 초기화도 됨.
//		System.out.print(score[0]);
//		System.out.print(score[1]);
//		System.out.print(score[2]);
//		System.out.print(score[3]);
//		System.out.print(score[4]);
//		System.out.println(score); // 주소값 출력
		
	}

}
