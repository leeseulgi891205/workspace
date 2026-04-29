package J0130_01;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Scanner;

public class SutMain {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		StuDeck s = new StuDeck();
		
	loop:while(true) {
		
		s.screen();//화면출력
		
		int choice = scan.nextInt();
		
		switch(choice) {
		case 1:
			s.stu_input();
			break;
		case 2:
			s.stu_output();
			break;
		case 3:
			s.stu_update();
			break;
		case 4:
			s.stu_delete();
			break;
		case 5:
			s.stu_search();
			break;
		case 6: // 성적정렬
			s.stu_sort(choice);
			s.stu_output();
			break;
		case 8:
			s.fileOpen();
			break;
		case 9:
			s.fileSave();
			break;
		case 0:
			System.out.println("프로그램을 종료합니다.");
			break loop;
		}//switch
	}//while
		
		
		

		
		
		
		
		
		
		
		
	}
}