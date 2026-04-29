package j0120_01;

import java.util.Scanner;

public class C0120_02 {

	public static void main(String[] args) {
		
		// 조건문 - if,switch
		// 반복문 - for,while
		
//		String num = "100";
		int no = 10;
		String name = "홍길동";
		int num = 100;
		String a = String.format("번호:%d, 이름:%s, 국어:%d \n ", no,name,num);
		System.out.println(a);
//		String b = System.out.printf("%010d \n",num);
		
		
//		int num = 100;
//		System.out.printf("%10d \n",num);
//		System.out.printf("%010d \n",num);
		
//		int i = 10;
//		String name = "홍길동";
//		double avg = 99.6799999;
//		//"번호:10, 이름:홍길동, 평균:99.67"
//		System.out.printf("번호:%d, 이름:%s, 평균:%.2f \n",i,name,avg);
		
		
//		int i=0;
//		int sum = 0;
//		while(true) {
//			if(sum>100) {
//				break;
//			}
//			sum += i;
//			i++;
//		}
//		System.out.println("i-1의 값 : "+(i-1));
//		System.out.printf("%d-1의 sum의 값 : %d \n",i,sum-i);
//		
//		System.out.println("i의 값 : "+i);
//		System.out.println("sum의 값 : "+sum);
		
		//무한반복
//		for(;;) {
//			break;
//		}
		
		
		
		
		
//		int i=0;
//		//반복문 이름 지정가능
//		loop:while(true) {
//			while(i<10) {
//				if(i==0) {
//					break loop; //반복문을 종료하는 것.
//				}
//			}
//			
//		}
//		
//		
//		loop2:for(i=0;i<9;i++) {
//			
//		}
		
		
		
		
//		int i = 11;
//		do {
//			System.out.println("실행");
//			i++;
//		}while(i<10);
		
		
//		while(i<10) {
//			System.out.println("실행");
//			i++;
//		}
		
		
		
		
//		Scanner scanner = new Scanner(System.in);
//		
//		int ran_num = (int)(Math.random()*100)+1;
//		
//		for(int i=0;i<10;i++) {
//			System.out.println("랜덤숫자를 맞춰 보세요. 숫자입력 >> ");
//			int input = scanner.nextInt();
//			if(ran_num>input) {
//				System.out.println("입력한 수보다 큰수입니다.");
//			}else if(ran_num<input) {
//				System.out.println("입력한 수보다 작은수입니다");
//			}else {
//				System.out.println("정답입니다.");
//				break;
//			}
//		}
//		
//		System.out.println("랜덤숫자 정답 : "+ran_num);
		
//		int i=0;
//		while(i<10) {
//			System.out.println("랜덤숫자를 맞춰 보세요. 숫자입력 >> ");
//			int input = scanner.nextInt();
//			if(ran_num>input) {
//				System.out.println("입력한 수보다 큰수입니다.");
//			}else if(ran_num<input) {
//				System.out.println("입력한 수보다 작은수입니다");
//			}else {
//				System.out.println("정답입니다.");
//				break;
//			}
//			i++;
//		}
		
//		System.out.println("랜덤숫자 정답 : "+ran_num);
		
		// 1~100까지의 랜덤숫자를 생성해서
		// 10번 시도해서 맞추는 프로그램을 while,for문 둘다 구현하시오.
		
		// 1번째 시도입니다.
		// 번호를 입력했을때 
		// 입력한 수보다 큰수입니다. 입력한 수보다 작은수입니다. 정답입니다.
		
		// 랜덤숫자 정답 : 7
		
		
		
		
		
		
		// 입력을 2개 받아 구구단 출력하시오.
		// 3,7 -> 3단에서 7단까지 출력
//		System.out.println("숫자1를 입력하세요.>> ");
//		int input1 = scanner.nextInt();
//		System.out.println("숫자2를 입력하세요.>> ");
//		int input2 = scanner.nextInt();
//		int num1 = (input1<input2?input1:input2);
//		int num2 = (input1>input2?input1:input2);
//		int num1 = Math.min(input1, input2);
//		int num2 = Math.max(input1, input2);
		
//		for(int i=num1;i<=num2;i++) {
//			System.out.printf("[ %d 단 ]\n",i);
//			for(int j=1;j<=9;j++) {
//				System.out.printf("%d X %d = %d\n",i,j,(i*j));
//			}
//			System.out.println();
//		}
		
		
		
		
		
		
//		int i=0; //초기값
//		while(i<=9) { //조건식
//			int j=0;
//			while(j<=9) {
//				int k=0;
//				while(k<=9) {
//					System.out.printf("%d%d%d\n",i,j,k);
//					k++;
//				}
//				j++;
//			}
//			i++; //증감식
//		}
		
		
//		for(int i=0;i<=9;i++) 
//			for(int j=0;j<=9;j++) 
//				for(int k=0;k<=9;k++) 
//					System.out.printf("%d%d%d\n",i,j,k);				
				
		
		
		// 배열
//		System.out.println("이름을 입력하세요.>> ");
//		String name = scanner.next();
//		System.out.println("국어점수를 입력하세요.>> ");
//		int kor = scanner.nextInt();
//	    System.out.println("이름을 입력하세요.>> ");
//		String name2 = scanner.next();
//		System.out.println("국어점수를 입력하세요.>> ");
//		int kor2 = scanner.nextInt();
//		
//		// 2명의 성적을 모두 출력하시오.
//		System.out.printf("%s\t%d\n",name,kor);
//	    System.out.printf("%s\t%d\n",name2,kor2);
		
		
		
		
		
		// 구구단을 출력하는데 2,4,6,8단 짝수단만 출력하시오.
//		for(int i=2;i<=9;i++) {
//			System.out.printf("[ %d 단 ] \t",i);
//		}
//		System.out.println();
//		for(int i=1;i<=9;i++) {
//			for(int j=2;j<=9;j++) {
//				System.out.printf("%d X %d = %d\t",j,i,(i*j));
//			}
//			System.out.println();
//		}
		
		
		
		
		
		
//		for(int i=2;i<=9;i++) {
//			if(i%2!=0) continue;
//			System.out.printf("[ %d 단 ]\n",i);
//			for(int j=1;j<=9;j++) {
//				if(j%2==0) continue;
//				System.out.printf("%d X %d = %d\t",i,j,(i*j));
//			}
//			System.out.println();
//		}
		
		
		
		
		// 중첩for문
//		for(int i=2;i<=9;i++) {
//			System.out.printf("[ %d 단 ]\n",i);
//			for(int j=1;j<=9;j++) {
//				System.out.printf("%d X %d = %d\t",i,j,(i*j));
//			}
//			System.out.println();
//		}

	}

}
