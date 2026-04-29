package j0119_01;

import java.util.Scanner;

public class C01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("[학생성적입력프로그램]");
		System.out.println("1. 학생성적입력");
		System.out.println("2. 학생성적출력");
		System.out.println("3. 학생성적수정");
		int choice = scanner.nextInt();
		
		if(choice==1) {
			System.out.println("학생성적입력");
		}else if(choice==2) {
			System.out.println("학생성적출력");
		}else if (choice==3) {
			System.out.println("학생성적수정");
		}else {
			System.out.println("잘못된 선택입니다.");
		}
		
//		switch(choice){
//		case 1:
//			System.out.println("학생성적입력");
//			break;
//		case 2:
//			System.out.println("학생성적출력");
//			break;
//		case 3:
//			System.out.println("학생성적수정");
//			break;
//		default:
//			System.out.println("잘못된 선택입니다.");
//			break;
//		}

	}

}
