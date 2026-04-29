package j0122_01;

import java.util.Scanner;

public class C1222_09 {
	static Scanner scanner = new Scanner(System.in); //인스턴스 변수-객체선언후 참조변수명.변수명
	
	static int stuInput() {
		int kor = 0;
		System.out.println("국어점수를 입력하세요.>> ");
		kor = scanner.nextInt();
		//영어점수,수학점수
		return kor;
		
	}
	
	public static void main(String[] args) {
		
		int[] score = new int[3];
		
		// kor,eng,math점수를 출력하시오.
//		System.out.println(stuInput());
		
		
		
		
//		//객체선언
//		MainMethod m = new MainMethod();
//		
//		//주소값 매개변수 전달하면 값이 변경됨.
//		Stuscore[] stuArr = new Stuscore[3];
//		m.stuInput(stuArr);
//		m.stuOutput(stuArr);
		

	}

}
