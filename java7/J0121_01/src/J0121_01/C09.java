package J0121_01;

import java.util.Scanner;

public class C09 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		// 변수선언
		String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
		int[] no = new int[10];
		String[] name = new String[10];
		int[][] score = new int[10][4];
		double[] avg = new double[10];
		int total = 0, count = 0;
		
		loop:while(true) {
			// 화면출력
			System.out.println("[ 학생생적프로그램 ]");
			System.out.println("1. 성적입력");
			System.out.println("2. 성적출력");
			System.out.println("3. 성적수정");
			System.out.println("4. 성적검색");
			System.out.println("0. 종료");
			System.out.println("-------------------");
			System.out.print("원하는 번호를 입력하세요.>> ");
			int choice = scanner.nextInt();
			
			switch(choice) {
			case 1: // 성적입력
				while(true) {
					total = 0; //초기화
					System.out.println("[ 학생성적입력 ]");
					System.out.printf("%d번째 학생이름을 입력하세요.(0.이전페이지이동)>> ",count+1);
					name[count] = scanner.next();
					
					// 0 입력시 이전페이지 이동
					if(name[count].equals("0")) break;
					
					for(int i=0;i<3;i++) {
						//국어,영어,수학
						System.out.printf("%s 점수를 입력하세요. >> ",title[i+2]);
						score[count][i] = scanner.nextInt();
						// 합계
						total += score[count][i];
					}
					//합계
					score[count][3] = total;
					//평균
					avg[count] = total/3.0;
					no[count] = count+1;
					count++;
					System.out.println("학생성적이 입력되었습니다.");
					System.out.println();
				}
				break;
				
			case 2: // 성적출력
				System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
				System.out.println("-------------------------------------------------------------------------------------------");
				for(int i=0;i<count;i++) {
					System.out.printf("%d\t",no[i]);           //번호
					System.out.printf("%s\t",name[i]);         //이름
					for(int j=0;j<score[0].length;j++) {
						System.out.printf("%d\t",score[i][j]); // [0,0][0,1][0,2][0,3]
					}
					System.out.printf("%.2f\n",avg[i]);        //평균
				}
				System.out.println();
				break;
			case 3: //학생수정
				
				
				
				
				
				break;
			case 4: //학생검색
				System.out.println("[ 학생검색 ]");
				
				System.out.println("검색할 학생이름을 입력하세요.>> ");
				String search = scanner.next();
				int temp = 0;
				System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
				System.out.println("-----------------------------------------------------------");
				for(int i=0;i<count;i++) { // 유관순 -> 홍길동,유관순,이순신,홍길자,홍길순
//					if (name[i].equals(search)) { //이름과 동일하면 출력
					if (name[i].contains(search)) { //이름과 동일하면 출력
						temp = 1;
						System.out.printf("%d\t",no[i]);           //번호
						System.out.printf("%s\t",name[i]);         //이름
						for(int j=0;j<score[0].length;j++) {
							System.out.printf("%d\t",score[i][j]); // [0,0][0,1][0,2][0,3]
						}
						System.out.printf("%.2f\n",avg[i]);        //평균						
					}
					
				}
				if(temp==0) System.out.println("검색된 학생이 없습니다.");
				System.out.println();
				break;
			default:
				System.out.println("[ 프로그램 종료 ]");
				System.out.println("프로그램을 종료합니다.");
				break loop;
			}
		}
		
		
		// 검색.
//		int[] a = {1,2,0,4,0,12,3,4,0,9,0,34,1};
//		int temp = 0;
//		int count = 0;
//		for(int i=0;i<a.length;i++) {
//			if(a[i]==0) {
//				System.out.println("해당문자가 있습니다.");
//				count++;
//				temp = 1;
//			}
//		}
//		
//		if(temp==0) {
//			System.out.println("해당문자가 없습니다.");
//		}else {
//			System.out.println("해당문자 개수 : "+ count);
//		}
		
		
		
//		int[] a = {1,2,3,4,5};
//		for(int i=0;i<a.length;i++) {
//			System.out.print(a[i]+"\t");
//		}
//		System.out.println();
//		System.out.println("개수 : "+a.length);
//		
//		for(int i=a.length-1;i>=0;i--) {
//			System.out.print(a[i]+"\t");
//		}
//		System.out.println();
		

	}

}