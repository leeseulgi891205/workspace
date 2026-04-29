package J0123_01;

import java.util.Scanner;

public class C08 {
	

	public static void main(String[] args) {
		Stuscore[] s = new Stuscore[10];
		Scanner scanner = new Scanner(System.in);
		System.out.println("[학생성적프로그램]");
		System.out.println("1.학생성적입력");
		System.out.println("--------------------");
		System.out.print("원하는 번호를 입력하세요.>>");
		int choice = scanner.nextInt();
		switch(choice) {
		case 1:
			while(true) {
				System.out.print("이름을 입력하세요.(0.이전페이지)>>");
				String name = scanner.next();
				if(name.equals("0")) {
					System.out.println("이전페이지로 이동합니다.");
					break;
				}
				int kor = 0, eng = 0, math = 0;
				System.out.println("국어점수를입력하세요.>>");
				kor = scanner.nextInt();
				System.out.println("영어점수를입력하세요.>>");
				eng = scanner.nextInt();
				System.out.println("수학점수를입력하세요.>>");
				math = scanner.nextInt();
				s[Stuscore.count] = new Stuscore(name,kor,eng,math);
				System.out.println("");
				System.out.printf("%s,%s,%d,%d,%d,%d,%.2f%n",
					s[Stuscore.count-1].no,
					s[Stuscore.count-1].name,
					s[Stuscore.count-1].kor,
					s[Stuscore.count-1].eng,
					s[Stuscore.count-1].math,
					s[Stuscore.count-1].total,
					s[Stuscore.count-1].avg);
				
				for(int i=0;i<Stuscore.count+1;i++) {
					System.out.printf(
					"%d,%s,%d,%d,%d,%d,%.2f\n",		
						s[i].no,s[i].name,s[i].kor,
						s[i].eng,s[i].math,s[i].total,
						s[i].avg);
				}

			}
			break;
		}
		System.out.println("프로그램을 종료합니다.");
	}
}
