//package J01027_01;
//
//import java.util.Scanner;
//
//public class C02 {
//
//	public static void main(String[] args) {
//		Scanner scan = new Scanner(System.in);
//		StuDeck s = new StuDeck();
//		
//		loop:while (true) {
//			s.stuPrint();//화면출력부분
//			
//			int choice = scan.nextInt();
//			
//			switch (choice) {
//			case 1:
//				s.stuInput();//학생성적입력부분
//				break;
//			case 2:
////				s.stuOutput();			
//				break;
//			case 3:
////				s.stuUpdate();
//				break;
//
//			case 0:
//				System.out.println("프로그램을 종료합니다.");
//				System.out.println();
//				break loop;
//
//			}
//		}
//	}
//
//}