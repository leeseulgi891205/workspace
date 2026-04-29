package j0128;

import java.util.Scanner;

public class C08 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		StuDeck s = new StuDeck();
		
		loop:while(true) {
			s.screen_print(); //출력화면
			int choice = scan.nextInt();
			switch(choice) {
			case 1://입력
				s.stuInput();  //학생성적입력
				break;
			case 2:
				s.stuOutput(); //학생성적출력
				break;
			case 4:
				s.stuDelete(); //학생성적삭제
				break;
			case 0:
				System.out.println("[ 프로그램 종료 ]");
				System.out.println();
				break loop;
			}
		}
		
		
		
//		Stuscore s = new Stuscore();
//		s.setKor(50);
//		s.setKor(500);
//		s.kor = 500;
//		System.out.println(s.getKor());

	}

}
