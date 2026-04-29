package J0122_01;

import java.util.Scanner;

public class C01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		while(true) {
			String[] title = {"번호","이름","국어","영어","수학","합계","평균"};
			int[] no = {1,2,3,0,0,0,0,0,0,0};
			String[] name = {"홍길동","유관순","김유신","","","","","","",""};
			int[][] score = {
					{100,100,100,300},{90,90,90,270},
					{80,80,80,240},{0,0,0,0},{0,0,0,0},
					{0,0,0,0},{0,0,0,0},{0,0,0,0},
					{0,0,0,0},{0,0,0,0}
					
			};
			double[] avg = {100.0,90.0,80.0,0.0,0.0,0.0,0,0};
			int  count = 3;
			String search = "";
			int temp = 0, choice = 0;
					
		loop:while(true) {
			// 화면출력
			System.out.println("[ 학생생적프로그램 ]\n");
			System.out.println("1. 성적입력");
			System.out.println("2. 성적출력");
			System.out.println("3. 성적수정");
			System.out.println("4. 성적검색");
			System.out.println("0. 종료");
			System.out.println("-------------------");
			System.out.print("원하는 번호를 입력하세요.>> ");
			choice = scanner.nextInt();
			
			switch(choice) {
			case 1:// 성적입력
				while(true) {// 무한반복
					System.out.println("[ 학생성적입력 ]");// 학생성적입력
					int total = 0; //초기화
					no[count] = count+1;// 번호저장
					System.out.printf("%d번째 학생이름을 입력하세요.(0.이전페이지이동)>> ",count+1);
					name[count] = scanner.next();			
					// 0 입력시 이전페이지 이동
					if(name[count].equals("0")) {
						System.out.println(">> 이전페이지로 이동합니다.");
						System.out.println();
						break;
					}
					
					
					for(int i=0;i<3;i++) {
						//국어,영어,수학
						System.out.printf("%s 점수를 입력하세요. >> ",title[i+2]);
						score[count][i] = scanner.nextInt();
						// 합계
						total += score[count][i];
					}
					//합계
					score[count][3] = total;// 합계저장
					//평균
					avg[count] = total/3.0;// 평균계산
					System.out.println("학생성적이 입력되었습니다.");// 입력완료메세지
					System.out.println();// 한줄띄우기
					count++;
				}
				break;
			case 2:// 성적출력
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
				// 수정학생이름 검색
				System.out.println("수정하려는 학생이름을 입력하세요.>>");
				search = scanner.next();
				temp = 0;
				for (int i=0;i<count;i++) {
					// 검색확인
					if(name[i].equals(search)) {
						System.out.printf("%s 학생의 성적을 수정합니다.\n",search);
						System.out.println("1. 국어점수 수정");
						System.out.println("2. 영어점수 수정");
						System.out.println("3. 수학점수 수정");
						System.out.print("---------------------------\n");
						System.out.print("수정할 과목을 선택하세요.>> ");
						choice = scanner.nextInt();
						System.out.println();
						
						// 국어,영어,수학 점수 수정
						System.out.printf("[ %s 점수 수정 ]\n",title[choice+1]);
						System.out.printf("현재 %s점수 : %d \n",title[choice+1],score[i][choice-1]);
						System.out.printf("변경 %s점수를 입력하세요.>>",title[choice+1]);
						score[i][choice-1] = scanner.nextInt();
						
						// 합계,평균수정
						score[i][3] = score[i][0]+score[i][1]+score[i][2];
						avg[i] = score[i][3]/3.0;
						temp=1;
						
						System.out.printf("%s 학생 %s 점수가 %d으로 수정되었습니다.\n",search,title[choice+1],score[i][choice-1]);
						System.out.println();
						
						

						}
						break;
					}// if 끝
					if (temp==0) {
						System.out.printf("수정하려는%s 학생을 찾지 못했습니다...",search);
						System.out.println();
				}
				
				break;
			case 4: //학생검색
				// 학생이름검색
				System.out.println("검색하려는 학생이름을 입력하세요.>>");
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
						break;
					}// if 끝
				}
				System.out.println();
				// 검색되지 않았을때
				if(temp==0) {
					System.out.printf("%s 학생이 검색되지않았습니다.",search);
					System.out.println();
				}
				break;
			case 0:
				System.out.println("[프로그램을 종료합니다]");
				break loop;
			}// switch 끝
		}// while 끝
		
		// 변수선언
		
		}// while 끝
	}// main 끝
}// class 끝
