package J0121_01;

import java.util.Scanner;

public class C07 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		//1-100번 사이의 랜덤 번호를 생성해서
		//10번 기회에 번호를 맞추는 프로그램을 구현하시오.
		//정답을 맞추면 프로그램을 종료하고
		//입력한 번호 : 50 30 40 43 45
		//도전횟수 : 5번
		//정답번호 : 45번
		// 1~100 랜덤 정답 생성
		int num = (int)(Math.random()*100) + 1;
		int count = 0;                 // 도전 횟수
		String inputNum = "";         // 입력한 숫자 기록용
		while (count<10) {	// 최대 10번 도전
			System.out.print((count+1)+"번째 숫자를 입력하세요.>> ");	// 몇 번째 도전인지 출력
			int input = scanner.nextInt();	// 사용자 입력
			count++;	// 도전 횟수 증가
			inputNum +=input + " ";  // 입력한 숫자 누적
			if (input == num) {
				System.out.println("정답입니다!");	// 정답 맞춤
				System.out.println("입력한 번호 : "+inputNum);	// 입력한 번호 출력
				System.out.println("도전횟수 : " +count+"번");	// 도전 횟수 출력
				System.out.println("정답번호 : " +num+"번");	// 정답 번호 출력
				scanner.close();
				return; // 정답 맞추면 프로그램 종료
			} else if (input > num) {
				System.out.println("더 작은 수를 입력하세요.");	// 입력한 수가 정답보다 큼
			} else {
				System.out.println("더 큰 수를 입력하세요.");		// 입력한 수가 정답보다 작음
			}
		}
		// 10번 안에 못 맞춘 경우
		System.out.println("5번의 기회를 모두 사용했습니다.");	// 기회 소진 안내
		System.out.println("입력한 번호 : "+inputNum);	// 입력한 번호 출력
		System.out.println("정답번호 : "+num+"번");	// 정답 번호 출력
		/**

	}
}
