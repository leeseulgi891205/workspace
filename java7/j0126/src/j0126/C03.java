package j0126;

import java.util.Scanner;

public class C03 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		//배열선언
		Stuscore[] s = new Stuscore[10];
		//학생성적입력
		System.out.println("학생이름을 입력하세요.>> ");
		String name = scanner.next();
		System.out.println("국어점수를 입력하세요.>> ");
		int kor = scanner.nextInt();
		System.out.println("영어점수를 입력하세요.>> ");
		int eng = scanner.nextInt();
		System.out.println("수학점수를 입력하세요.>> ");
		int math = scanner.nextInt();
		// 배열에 객체저장
		s[0] = new Stuscore(name,kor,eng,math);
		System.out.println("학생이 저장되었습니다.");
		
		System.out.printf("%d,%s,%d,%d,%d,%d,%.2f\n",
				s[0].no,s[0].name,s[0].kor,s[0].eng,s[0].math,
				s[0].total,s[0].avg);
		
		
		
		
		// 배열선언
//		Stuscore[] s = new Stuscore[10];
//		s[0] = new Stuscore("홍길동",100,100,99);
//		s[1] = new Stuscore("유관순",90,90,95);
//		s[2] = new Stuscore("이순신",80,80,81);
		
		// 개별적인 객체선언
//		Stuscore s1 = new Stuscore();
//		s1.name = "홍길동";
//		s1.kor = 100;
//		s1.eng = 100;
//		s1.math = 99;
//		s1.total = (100+100+99);
//		s1.avg = s1.total/3.0;
//		System.out.println(s1.no+","+s1.name);
//		Stuscore s2 = new Stuscore("유관순",100,100,99);
//		System.out.println(s2.no+","+s2.name);
//		Stuscore s3 = new Stuscore("이순신",90,90,91);
//		System.out.println(s3.no+","+s3.name);
	}
}
