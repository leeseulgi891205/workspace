package J0121_01;



public class C03 {

	public static void main(String[] args) {
		// 5행 5열을 2차원 배열로 1~25까지 순차적인 번호를 입력해서 출력하시오.
		
		// 2차원 [5][5] 랜덤배열로 출력하시오.
		int[][] score = new int[5][5];
		// 값 넣기 (랜덤)
		for (int i = 0; i < score.length; i++) {
			for (int j = 0; j < score[i].length; j++) {
				score[i][j] = (int)(Math.random() * 100) + 1; // 1~100 랜덤
			}
		}
		// 출력부분
		for (int i = 0; i < score.length; i++) {
			for (int j = 0; j < score[i].length; j++) {
				System.out.printf("%3d ", score[i][j]);
			}
			System.out.println();
		}
		System.out.println();
		
		
		
		
		
		
		
		
		int [][] score2 = new int[5][5];
		int[] num = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25};
		for (int i=0;i<score2.length;i++) {
			for (int j=0;j<score2[i].length;j++) {
				score2[i][j] = num[(i*5)+j];
			}
		}
		// 출력부분
		for (int i=0;i<score2.length;i++) {
			for (int j=0;j<score2[i].length;j++) {
				System.out.printf("%2d ",score2[i][j]);
			}
			System.out.println();
		}
		System.out.println();
		
		
		
		
		
		
		
		
		
		
		
//		int [] score = new int[5];
//		
//		for (int i=1;i<score.length;i++) {
//			for (int j=1;j<=5;j++) {
//				System.out.printf("%2d ",(i-1)*5+j);
//			}
//			System.out.println();
//		}
//		System.out.println();
		
		
		
		
		
		
		
		
		
		
		
		// 2차원 [5][5] 배열
		// 1-25 출력
		// 3행 2열, 5행 1열, 2행 4열 5행 5열 출력
		
		
		
		
		
		
		
		
		
		
//		int [][] score = {
//				{ 1, 2, 3, 4, 5},
//				{ 6, 7, 8, 9,10},
//				{11,12,13,14,15},
//				{16,17,18,19,20},
//				{21,22,23,24,25}
//
//		};
//		for(int i=0;i<score.length;i++) {
//			for(int j=0;j<score[i].length;j++) {
//				System.out.print(score[i][j]+"\t");
//			}
//			System.out.println();
//		}
//		
//		// 3행 2열, 5행 1열, 2행 4열 5행 5열 출력
//		System.out.println("3행 2열 : "+score[2][1]);
//		System.out.println("5행 1열 : "+score[4][0]);
//		System.out.println("2행 4열 : "+score[1][3]);
//		System.out.println("5행 5열 : "+score[4][4]);
//		System.out.println();
		
		
		
		
		
		
		
		
		
//		// 1차원 배열
//		int [] a = {1,2,3,4,5};
//		for(int i=0;i<a.length;i++) {
//			System.out.print(a[i]+"\t");
//		}
//		System.out.println();
//		
//		
//		// 2차원 배열
//		int [][] score = {
//				{100,100,100},
//				{90,90,90},
//				{80,80,80}
//		};
//		for(int i=0;i<score.length;i++) {
//			for(int j=0;j<score[i].length;j++) {
//				System.out.print(score[i][j]+"\t");
//			}
//			System.out.println();
//		}

	}

}