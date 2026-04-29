package j0121_01;

import java.util.Arrays;

public class C0121_03 {

	public static void main(String[] args) {
		
		//5행5열을 1~25까지 순차적인 번호를 입력해서 출력하시오.
		int[] num = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25};
		
		
		int[][] score = new int[5][5];
		// 1.번호넣기
		for(int i=0;i<score.length;i++) {
			for(int j=0;j<score[i].length;j++) {
				score[i][j] = num[i*5+j]; //0,1,2...24
				//score[i][j] = (i*5)+j+1;
			}
		}
		
		//
		for(int i=0;i<score.length;i++) {
			for(int j=0;j<score[i].length;j++) {
				System.out.print(score[i][j]+"\t");
			}
			System.out.println();
		}
		
		// [ 1차원 배열 순차적으로 번호 입력후 출력 ]
//		int[] score = new int[5];
//		
//		for(int i=0;i<score.length;i++) {
//			score[i] = i+1;
//		}
//		
//		for(int i=0;i<score.length;i++) {
//			System.out.print(score[i]+"\t");
//		}
		
		
		
		
		
		
		
		// 2차원 [5][5]
		// 1-25 값을 입력해서 출력하시오.
		// 3행 2열, 5행 1열, 2행 4열, 5행 5열
//		int[][] score = {
//				{1,2,3,4,5},
//				{6,7,8,9,10},
//				{11,12,13,14,15},
//				{16,17,18,19,20},
//				{21,22,23,24,25},
//		};
//		for(int i=0;i<score.length;i++) {
//			for(int j=0;j<score[i].length;j++) {
//				System.out.print(score[i][j]+"\t");
//			}
//			System.out.println();
//		}
//		
//		//3행 2열, 5행 1열, 2행 4열, 5행 5열
//		System.out.println(score[2][1]);
//		System.out.println(score[4][0]);
//		System.out.println(score[1][3]);
//		System.out.println(score[4][4]);
		
		
		
//		// 1차원 배열
//		int[] a = {1,2,3,4,5};
//		for(int i=0;i<a.length;i++) {
//			System.out.print(a[i]+"\t");
//		}
//		System.out.println();
//		
//		// 2차원 배열
//		int[][] score = {
//				{100,100,100},
//				{90,90,90},
//				{80,80,80},
//		};
//		for(int i=0;i<score.length;i++) {
//			for(int j=0;j<score[i].length;j++) {
//				System.out.print(score[i][j]+"\t");
//			}
//			System.out.println();
//		}

	}

}
