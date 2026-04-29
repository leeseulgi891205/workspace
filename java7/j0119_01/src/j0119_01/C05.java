package j0119_01;

import java.util.Scanner;

public class C05 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("음료선택을 하세요..>>");
		System.out.println("1. 아메리카노.>>");
		System.out.println("2. 바닐라라떼.>>");
		System.out.println("3. 아이스티.>>");
		System.out.println("원하는 번호를 선택하세요.>>");
		
		
		int input = scanner.nextInt();
		
		switch(input) { 
		case 1:
			System.out.println("아메리카노를 선택하셨습니다.");
			// 2분
			break;
		case 2:
			System.out.println("바닐라라떼를 선택하셨습니다.");
			// 3분
			break;
		case 3:
			System.out.println("아이스티를 선택하셨습니다.");
			// 1분 40초
			break;
		}
		
		scanner.close();
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
//		// 98점이상 A+, 97~94 A 93 A-
//		// 88이상 B+, 87~84 B 83 B-
//		// 77이상 C+...
//		// 66이상 D+
//		// 60미만 F
//		// 출력하시오
//		System.out.print("점수를 입력하세요 >> ");
//		int score = scanner.nextInt();
//		if (score>=98) {
//			System.out.println("A+ 대단한데요? 서울대 갑시다!!");
//			}else if (score>=94) {
//			System.out.println("A 잘했어요!");
//			}else if (score>=93) {
//			System.out.println("A- 더 잘할거에요.");
//			}else if (score>=88) {
//			System.out.println("B+ 좀 더 노력하세요.");
//			}else if (score>=84) {
//			System.out.println("B 나쁘지 않아요.");
//			}else if (score>=83) {
//			System.out.println("B- 노력하세요.");
//			}else if (score>=77) {
//			System.out.println("C+ 꾸준히 하세요.");
//			}else if (score>=74) {
//			System.out.println("C 보통이네요.");
//			}else if (score>=73) {
//			System.out.println("C- 조금만 더 힘내세요.");
//			}else if (score>=66) {
//			System.out.println("D+ 조금만 더 분발하세요.");
//			}else if (score>=64) {
//			System.out.println("D 힘내세요.");
//			}else if (score>=60) {
//			System.out.println("D- 조금만 더 노력하세요.");
//			}else {
//			System.out.println("F 뭐하세요? 공부안해요?");
//			}
		
		
		
		
		
		
		
		
		
		
		
		// if문으로 19854 -> 7이 몇개 있는지 출력하시오. 
		// 문자열 -> charAt()
//		int count = 0;
//		System.out.print("숫자를 입력하세요 >> ");
//		String num = scanner.next();
//		if (num.charAt(0)=='7') count++;
//		if (num.charAt(1)=='7') count++;
//		if (num.charAt(2)=='7') count++;
//		if (num.charAt(3)=='7') count++;
//		if (num.charAt(4)=='7') count++;
//		System.out.println("7의 개수는 "+count+"개 입니다.");

		
		
		
		
		
		
//		System.out.print("숫자를 입력하세요 >> ");
//		int input = scanner.nextInt();
		
		//수(90점이상),우(80점이상),미(70점이상),양(60점이상),가(60점미만)
//		if(input>=90) {
//			System.out.println("수");
//			}else if(input>=80) {
//				System.out.println("우");
//				}else if(input>=70) {
//					System.out.println("미");
//					}else if(input>=60) {
//						System.out.println("양");
//						}else {
//							System.out.println("가");
//			}
		
		
		
		
		
		
		
		// 양수, 0 , 음수, if else if else
		//if(input>0) {
		//	System.out.println("양수");
		//}else if(input==0) {
		//	System.out.println("0");
		//}else {
		//	System.out.println("음수");
		//}
		
		
		
		
		
		
		
		
		
		
		//if(input>=60) {
		//	System.out.println("합격");
		//	System.out.println("축하합니다.");
		//}else{
		//	System.out.println("불합격");
		//	System.out.println("다음 기회에...");
		//}
		
		
		
		
		
		
		
		
		
		
	}

}
