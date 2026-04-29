package J0120_01;

import java.util.Scanner;

public class C02 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		// 조건문 - if, switch
		// 반복문 - for, while
		
		
//		String num = "100";
		int no = 10;
		String name = "홍길동";
		int num = 100;
		String a = String.format("번호:%d,이름:%s,국어:%d \n",no,name,num);
		System.out.println(a);
//		String b = System.out.printf("%010d \n",num);
		
		
		
//		int num = 100;
//		System.out.printf("%10d \n",num); // 오른쪽 정렬
//		System.out.printf("%-10d \n",num); // 왼쪽 정렬
//		System.out.printf("%010d \n",num); // 빈공간 0으로 채우기
		
		
		
		
		
		
//		int i = 10;
//		String name = "홍길동";
//		double avg = 99.6799999;
//		//"번호:10, 이름:홍길동,평균:99.67"
//		System.out.printf("번호:%d, 이름:%s, 평균:%.2f\n",i,name,avg);
		
		
		
		
		
		
//		int i=0;
//		int sum = 0;
//		while(true) {
//			sum += i;
//			i++;
//			if(sum>100)
//				break;
//		}
//		System.out.println("i-1의 값 : "+(i-1));
//		System.out.printf("%d-1의 sum의 값 : %d\n",i-1,sum);
//		
//		System.out.printf("i의 값 : %d\n",i);
//		System.out.printf("sum의 값 : %d\n",sum);
//		
//		for(;;) {
//			break;
//		}
		
		
		
		
		
		
		
		
		
		
		
		
		
//		int i = 0;
//		//반복문 이름 지정가능
//		while(true) { 
//		while(i<10) {
//			if(i==0) {
//			break; // 반복문을 종료하는 것.
//			}
//		}
//	}
//		
//		loop2:for(i=0;i<9;i++){
//			
//		}
		
		
		
		
		
		
		
		
//		int i = 11;
//		do{
//			System.out.printf("실행",i);
//			i++;
//		} while(i<10);
		
		
		
		
//		while(i<10) {
//			System.out.printf("실행");
//			i++;
//			break; // 반복문 탈출
//		}
		
		
		
		
		
		
		
		
		
		
		
		
		// 1~100까지의 랜덤숫자를 생성해서 10번시도해서 맞추는 프로그램을 구현하시오.
		// 시도횟수 : 10
		// 1번째 시도입니다.
		// whule구현하시오.
		// 번호를 입력했을때 입력한 수보다 큰수 입니다. 입력한 수보다 작은수입니다.
		// 정답입니다.
		// 시도횟수를 초과했습니다. 정답은 : 7
		
//		int rdom = (int)(Math.random()*100)+1; // 1~100까지 랜덤숫자 생성
//		int count = 0; // 시도횟수
//		int input = 0; // 사용자가 입력한 숫자
//		System.out.println("1~100사이의 숫자를 맞추세요.>>");
//		while(count < 10) {
//			count++; // 시도횟수 증가
//			System.out.printf("%d번째 시도입니다.>>",count);
//			input = scan.nextInt();
//			if(input < rdom) { 							// 입력한 수가 랜덤숫자보다 작을때
//				System.out.println("입력한 수보다 큰수 입니다."); 
//			} else if(input>rdom) { 					// 입력한 수가 랜덤숫자보다 클때 
//				System.out.println("입력한 수보다 작은수 입니다.");
//			} else { 									// 입력한 숫자가 랜덤숫자보다 작을때
//				System.out.println("정답입니다!!");
//				break;
//			}
//		}
//		if(count==10) {
//			System.out.printf("시도횟수를 초과했습니다. 정답은 : %d\n",rdom);
//		}
//		
		// 1~100까지의 랜덤숫자를 생성해서 10번시도해서 맞추는 프로그램을 구현하시오.
		// 시도횟수 : 10
		// 1번째 시도입니다.
		// for문으로 구현하시오.
		// 번호를 입력했을때 입력한 수보다 큰수 입니다. 입력한 수보다 작은수입니다.
		// 정답입니다.
		// 시도횟수를 초과했습니다. 정답은 : 7
		
//		int rdom2 = (int)(Math.random()*100)+1; // 1~100까지 랜덤숫자 생성
//		int input2 = 0; // 사용자가 입력한 숫자
//		System.out.println("1~100사이의 숫자를 맞추세요.>>");
		
//		for(int count2=1;count2<=10;count2++) {
//			System.out.printf("%d번째 시도입니다.>>",count2);
//			input2 = scan.nextInt();
//			if(input2 < rdom2) {
//				System.out.println("입력한 수보다 큰수 입니다.");
//			} else if(input2 > rdom2) {
//				System.out.println("입력한 수보다 작은수 입니다.");
//			} else {
//				System.out.println("정답입니다.");
//				break;
//			}
//			if(count2 == 10) {
//				System.out.printf("시도횟수를 초과했습니다. 정답은 : %d\n",rdom2);
//			}
//		}
		
		
		
		
		
		
		
		
		
		
		// 입력을 2개 받아 구구단 출력하시오.
		// 3,7 -> 3단에서 7단까지 출력하시오.
		
//		System.out.println("구구단을 입력하세요.>>");
//		int num = scan.nextInt();
//		System.out.println("구구단을 입력하세요.>>");
//		int num2 = scan.nextInt();
//		
//		
//		for(int i=num;i<=num2;i++) {
//			System.out.printf("[ %d단 ] \n",i);
//			if (i< num2) {
//				System.out.println();
//			}
//			for(int j=1;j<=9;j++) {
//				System.out.printf("%dx%d = %d\n",i,j,(i*j));
//			}
//			System.out.println();
//		}
		
		
		
		
		
		
		
//		int i = 0; // 초기값
//		while(i <= 999) { // 조건식
//			System.out.printf("%03d\n", i);
//			i++; // 증감식
//		}
		
		// 0~999까지 출력하시오. while문 사용
		
//		int i=0; // 초기값
//		int j=0; // 초기값
//		int k=0; // 초기값
//		while(i<=9) { // 조건식
//			j=0;	// 초기값
//			while(j<=9) { // 조건식
//				k=0;	// 초기값
//				while(k<=9) { // 조건식
//					System.out.printf("%d%d%d\n",i,j,k);
//					k++; // 증감식
//				}
//				j++; // 증감식
//			}
//			i++; // 증감식
//		}
		
		
//		for(int i=0;i<=9;i++) {
//			for(int j=0;j<=9;j++) {
//				for(int k=0;k<=9;k++) {
//					System.out.printf("%d%d%d\n",i,j,k);
//				}
//			}
//		}
		
		
		
		
		
		
		
		// 000
		// 001
		// 002
		// 999
//		for(int i=0;i<=9;i++) {
//			for(int j=0;j<=9;j++)
//				for(int k=0;k<=9;k++)
//			System.out.printf("%d%d%d\n",i,j);
//		}
		
		
		
		
		
		
		
//		for(int i=0;i<2;i++){
//			System.out.println("이름을 입력하세요.>>");
//			String name = scan.next();
//			System.out.println("국어점수를 입력하세요.>>");
//			int kor = scan.nextInt();
//			System.out.printf("%s,%d\n",name,kor);
//		}
//		
//		// 2명의 성적을 모두 출력하시오.
//		
//		System.out.println("%s\t%d\n");
		
		
		
		
		
		
		
		
		
		
		
//		// 구구단을 전체 출력하시오. 세로로 출력
//		
//		for (int j=1;j<=9;j++) { // 1~9까지 증가
//			System.out.printf("[ %d 단]\t",j); 
//			}
//			System.out.println();
//			for(int j=1;j<=9;j++) { // 1~9까지 증가
//			System.out.printf("\n"); // 줄바꿈
//			for(int i=2;i<=9;i++) { // 2~9단까지 증가
//				// 단 출력
//				System.out.printf("%d x %d = %d \t",i,j,(i*j));
//			}
//			System.out.println();
//		}

		
		
		
		
		
		
		
		
//		for(int i=2;i<=9;i++) {
//			if(i%2==0) continue;{ // 짝수단만 출력 사용법 : if(조건식)
//				System.out.printf("[ %d단 ] \n",i);
//				for(int j=1;j<=9;j++) {
//					if(j%2==0) continue; { // 홀수곱셈 제외 사용법 : if(조건식)
//					System.out.printf("%d x %d = %d \t",i,j,(i*j));
//				}
//				System.out.println();
//
//			}
//		}
		
		
		
		
		
		
		
		
		
		
		
//		// 중첩for문
//		for(int i=2;i<=9;i++) {
//			System.out.printf("[ %d단 ] \n",i);
//			for(int j=1;j<=9;j++) {
//				System.out.printf("%d x %d = %d \t",i,j,(i*j));
//			}
//			System.out.println();
//		}
	}

}