package j0122_01;

import java.util.Scanner;

public class C0122_01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		// 변수선언
		String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
		int[] no = {1,2,3,0,0,0,0,0,0,0};
		String[] name = {"홍길동","유관순","이순신","","","","","","",""};
		int[][] score = {
				{100,100,100,300},{90,90,90,270},{80,80,80,240},
				{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0},
				{0,0,0,0},{0,0,0,0},{0,0,0,0},
		};
		double[] avg = {100.0,90.0,80.0,0,0,0,0,0,0,0};
		int count = 3,temp = 0,choice = 0;
		String search = "";
		
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
			choice = scanner.nextInt();
			
			switch(choice) {
			case 1: //성적입력
				while(true) {
					System.out.println("[ 성적입력 ]");
					int total = 0; //합계초기화
					no[count] = count+1; //번호
					//이름입력
					System.out.printf("%d번째 학생이름을 입력하세요.(0.이전페이지 이동)>> ",count+1);
					name[count] = scanner.next();
					// 이전페이지 이동 체크
					if(name[count].equals("0")) {
						System.out.println(">> 이전페이지 이동합니다.");
						System.out.println();
						break;
					}
					
					// 국어,영어,수학
					for(int i=0;i<3;i++) {
						System.out.printf("%s 점수를 입력하세요.>> ",title[i+2]);
						score[count][i] = scanner.nextInt();
						total += score[count][i];
					}
					score[count][3] = total; //합계
					avg[count] = total/3.0;  //평균
					
					System.out.printf("%s 학생성적이 저장되었습니다.\n",name[count]);
					System.out.println();
					count++;
				}
				break;
			case 2:
				System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
				System.out.println("-----------------------------------------------------------");
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
			case 3:
				// 수정학생이름 검색
				System.out.println("수정하려는 학생이름을 입력하세요.>> ");
				search = scanner.next();
				temp = 0;
				for(int i=0;i<count;i++) {
					// 검색확인
					if(name[i].equals(search)) {
						System.out.printf("[ %s 학생 성적수정 ]\n",search);
						System.out.println("1. 국어점수 수정");
						System.out.println("2. 영어점수 수정");
						System.out.println("3. 수학점수 수정");
						System.out.println("------------------------");
						System.out.println("수정하려는 과목번호를 입력하세요.>> ");
						choice = scanner.nextInt();
						System.out.println();
						
						// 국어,영어,수학 점수수정
						System.out.printf("[ %s점수 수정 ]\n",title[choice+1]);
						System.out.printf("현재 %s점수 : %d \n",title[choice+1],score[i][choice-1]);
						System.out.printf("변경 %s점수를 입력하세요.>> ",title[choice+1]);
						score[i][choice-1] = scanner.nextInt();
						
						// 합계,평균수정
						score[i][3] = score[i][0]+score[i][1]+score[i][2];
						avg[i] = score[i][3]/3.0;
						temp=1;
						
						System.out.printf("%s학생 %s점수가 %d점으로 수정되었습니다.\n",search,title[choice+1],score[i][choice-1]);
						System.out.println();
					}//if
				}
				
				if(temp==0) {
					System.out.printf("수정하려는 %s 학생을 찾지 못했습니다!",search);
					System.out.println();
				}
				break;
			case 4: //학생검색
				// 학생이름검색
				System.out.println("검색하려는 학생이름을 입력하세요.>> ");
				search = scanner.next();
				temp = 0;
				// 검색출력시작
				System.out.printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",title[0],title[1],title[2],title[3],title[4],title[5],title[6]);
				System.out.println("-----------------------------------------------------------");
				for(int i=0;i<count;i++) {
					// 검색확인
					if(name[i].contains(search)) {
						System.out.printf("%d\t",no[i]);           //번호
						System.out.printf("%s\t",name[i]);         //이름
						for(int j=0;j<score[0].length;j++) {
							System.out.printf("%d\t",score[i][j]); // [0,0][0,1][0,2][0,3]
						}
						System.out.printf("%.2f\n",avg[i]);        //평균
						temp=1;
					}//if
				}
				System.out.println();
				// 검색되지 않았을때
				if(temp==0) {
					System.out.printf("%s 학생이 검색되지 않았습니다!",search);
					System.out.println();
				}
				
				break;
			case 0:
				System.out.println("[ 프로그램 종료 ]");
				break loop;
			}//switch
		}//while

	}//main
}//class
