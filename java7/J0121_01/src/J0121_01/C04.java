package J0121_01;

import java.util.Scanner;	

public class C04 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);	// 스캐너
		
		// 학생성적프로그램 - 이름,국어,영어,수학,합계
		String[] name = new String[2]; // 학생이름
		int[][] score = new int[2][4]; // 국어,영어,수학,합계
		double[] avg = new double[2]; // 평균
		String[] title = {"이름","국어","영어","수학","합계","평균"}; // 제목배열
		
		
		// 1. 성적입력부분
		int i =0; // 입력부분
		while(i<2) {
			System.out.println("이름을 입력하세요.>>");	// 이름입력
			name[i] = scanner.next();	// 이름저장
			int total = 0;				// 점수입력부분
			for(int j=0;j<3;j++) {
				System.out.printf("%s 점수를 입력하세요.>>\n",title[j+1]);	// 점수입력
				score[i][j] = scanner.nextInt();		// 점수저장
				total += score[i][j];					// 합계계산
			}
			score[i][3] = total;	// 합계저장
			avg[i] = total/3.0;		// 평균계산
			i++;
		}
		
		// 2. 성적출력부분
		
		// 제목출력
		System.out.println("         [학생성적프로그램]              ");
		System.out.println("=====================================");
		for(int j=0;j<title.length;j++) {		// 제목수
			System.out.print(title[j]+"\t");	// 제목출력
		}
		System.out.println();
		System.out.println("=====================================");
		
		
		// 이름,국어,영어,수학,합계
		for(int j=0;j<score.length;j++) {	// 학생수
			System.out.printf(name[j]+"\t");	// 이름출력
			for(int k=0;k<score[j].length;k++) {	// 점수출력
				// 국어,영어,수학,합계
				System.out.print(score[j][k]+"\t");	// 점수출력
			}
			// 평균출력
			System.out.printf("%.2f \n",avg[j]);
			
		}
		
		
		
		
		
		
		
		
		
		
		// 2차원 배열
//		int[][] score = new int[5][5]; // 25개 5,5 2차원 배열
//		int[] a = new int[25];
//		
//		int[][] num;
//		
//		// 1차원 입력
//		for(int i=0;i<a.length;i++) {
//			a[i] = i+1;
//		}
//		
//		
//		// 랜덤 섞기
//		for(int i=0;i<200;i++) {
//			int no = (int)(Math.random()*25); //0-24
//			int temp = a[0]; // 임시저장
//			a[0] = a[no]; // 랜덤번호의 값을 0번방에 입력
//			a[no] = temp; // 임시저장값을 랜덤방에 입력
//		}
//		
//		
//		// 2차원 입력
//		for(int i=0;i<score.length;i++) {
//			for(int j=0;j<score[i].length;j++) {
//				score[i][j] = a[5*i+j];	//1~25	//0,1,2,...24
////				score[i][j] = (i*5)+(j+1);	//1,2,3,....25
//			}
//		}
//		// 2차원 출력
//		for(int i=0;i<score.length;i++) {
//			for(int j=0;j<score[i].length;j++) {
//				System.out.print(score[i][j]+"\t");
//			}
//			System.out.println();
//		}
		
		
		
		
		
	}
	
		
		// 1차원 배열 - 랜덤으로 숫자 입력,출력
//		int[] a = new int[25]; // 1~25
		// 1차원배열 번호입력
////		int[] a = {1,2,3};
//		
//		for(int i=0;i<a.length;i++) {
//			a[i] = i+1;
//		}
//		
//		for(int i=0;i<200;i++) {
//			int no = (int)(Math.random()*25);
//			int temp = a[0];
//			a[0] = a[no];
//			a[no] = temp;
//		}
//		
//		
//		for(int i=0;i<a.length;i++) {
//			System.out.print(a[i]+"\t");
//		}
//
//	}
//
}
