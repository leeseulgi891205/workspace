package J0122_01;

import java.util.Scanner;

public class C09 {
	static Scanner scan = new Scanner(System.in); // 스캐너 객체선언
	
	 
	// 1. 함수 선언하기
	static int[] scoreInput() {
		int[] scores = new int[3]; // 국어,영어,수학 점수를 저장할 바구니
		System.out.print("국어점수 입력:");	// 국어점수 입력
		scores[0] = scan.nextInt();	// 국어점수 저장
		System.out.print("영어점수 입력:");	// 영어점수 입력
		scores[1] = scan.nextInt();	// 영어점수 저장
		System.out.print("수학점수 입력:");	// 수학점수 입력
		scores[2] = scan.nextInt();	// 수학점수 저장
		return scores; // 점수가 저장된 바구니를 반환
	}

	public static void main(String[] args) {
		// 2. 함수 호출하기
		int[] scores = scoreInput(); // 빈 바구니를 던져줌
		System.out.println("국어: "+scores[0]);	// scores[0] 국어점수
		System.out.println("영어: "+scores[1]);	// scores[1] 영어점수
		System.out.println("수학: "+scores[2]);	// scores[2] 수학점수
		
		
		
		
		
		
		
		
		
		
		
		
		// 객체선언
//		MainMethod m = new MainMethod();
//		
//		// 주소값 매개변수로 전달하면 값이 변경됨.
//		Stuscore[] stusArr = new Stuscore[3]; 
//		m.stuInput(stusArr); // 학생성적입력함수 호출
//		m.stuOutput(stusArr); // 학생성적출력함수 호출
	}

}
