package j0116_01;

import java.util.Scanner;

public class c05 {

	public static void main(String[] args) {
		//String 문자열타입: next()-사이띄움X(엔터불가), nextLine() -사이띄움가능 (엔터가능)
		//int 정수타입: nextInt(), nextLong()
		//double 실수타입: nextDouble(), nextFloat()
		Scanner scanner = new Scanner(System.in);
		// 이름,국어,영어,점수를 입력받아서 출력하시오 프린트f
		System.out.printf("이름을 입력하세요.>>\n");
		String name = scanner.nextLine();
		System.out.println("입력한 이름은 "+name+"입니다.");
		System.out.printf("국어점수를 입력하세요.>>\n");
		int kor = scanner.nextInt();
		System.out.println("입력한 국어점수는 "+kor+"입니다.");
		System.out.printf("영어점수를 입력하세요.>>\n");
		int eng = scanner.nextInt();
		System.out.printf("이름:%s 국어점수:%d 영어점수:%d\n",name,kor,eng);
		
		
		
		
		
		
		
		
		
		
		
		
		
		
//		System.out.printf("이름을 입력하세요.>>\n");
//		String name = scanner.next();
//		System.out.println("국어점수를 입력하세요.>>");
//		int kor = scanner.nextInt();
//		
//		System.out.println("이름: "+name+"국어점수:"+kor);
//		
		
//		System.out.printf("이름을 입력하세요.>>\n");
//		String name = scanner.nextLine();
//		scanner.nextLine(); //버퍼 비우기
//		System.out.println("입력한 이름은 "+name+"입니다.");
//		System.out.printf("아이디를 입력하세요.>>\n");
//		String id = scanner.nextLine();
//		System.out.println("입력한 아이디는 "+id+"입니다.");
	}

}
