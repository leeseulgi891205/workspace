package J0121_01;

import java.util.Scanner;

public class C10 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		// 학생 성적 프로그램을 출력하시오.
		String[] title = {"이름","국어","영어","수학","합계","평균"};
		int[] no = new int[5];
		String[] name = new String[5];
		int[][] score = new int[5][4];
		double[] avg = new double[5];
		int count = 0;
		
		while(true) {
			System.out.println("[학생성적프로그램입니다.]");
			System.out.println("1. 성적입력");
			System.out.println("2. 성적출력");
			System.out.println("3. 성적수정");
			System.out.println("4. 성적검색");
			System.out.println("5. 종료");
			System.out.println("----------------------");
			System.out.print("원하는 번호를 입력하세요.>>");
			int choice = scanner.nextInt();
			
			switch(choice) {
			case 1:
				if (count >= no.length) {
					System.out.println("더 이상 입력할 수 없습니다.");
					break;
				}
				System.out.println("[ 학생성적입력 ]");
				System.out.printf("%d번째 학생 이름을 입력하세요.>>",count+1);
				name[count] = scanner.next();
				int total = 0;
				for(int i=0;i<3;i++) {
					System.out.printf("%s 점수를 입력하세요.>>",title[i+1]);
					score[count][i] = scanner.nextInt();
					total += score[count][i];
					for(int j=0;j<score[count].length-1;j++) {
						score[count][3] = total;
						// 국어,영어,수학, 점수입력
						System.out.printf("%s 점수를 입력하세요.>>",title[j+1]);
						score[count][j] = scanner.nextInt();
						// 합계계산
						total += score[count][j];
					}
					// 합계저장
					score[count][3] = total;
					// 평균계산
					avg[count] = total/3.0;
					no[count] = count+1;
					count++;
					System.out.println("학생성적이 입력되었습니다.");
					break;
				}
			case 2:
				System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
				System.out.println("==========================================================================================");
				for(int i=0;i<count;i++) {
					System.out.printf("%d\t",no[i]);
					System.out.printf("%s\t",name[i]);
					for(int j=0;j<score[0].length;j++) {
						System.out.printf("%d\t",score[i][j]);
					}
					System.out.printf("%.2f\n",avg[i]);
					System.out.println();
				}
			}
		}
		

	}

}
